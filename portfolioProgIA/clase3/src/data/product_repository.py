import sqlite3
from typing import Any

from src.data.db import get_connection


class ProductRepository:
    def insert_product(self, nombre: str, codigo: int, precio: float, stock: int) -> dict[str, Any]:
        query = """
            INSERT INTO productos (nombre, codigo, precio, stock)
            VALUES (?, ?, ?, ?)
        """
        try:
            with get_connection() as conn:
                cursor = conn.execute(query, (nombre, codigo, precio, stock))
                conn.commit()
                return {
                    "id": cursor.lastrowid,
                    "nombre": nombre,
                    "codigo": codigo,
                    "precio": precio,
                    "stock": stock,
                }
        except sqlite3.IntegrityError as exc:
            if "UNIQUE constraint failed" in str(exc):
                raise ValueError("Ya existe un producto con ese codigo.") from exc
            raise ValueError("No se pudo guardar el producto por una restriccion de datos.") from exc

    def list_products(self) -> list[dict[str, Any]]:
        query = """
            SELECT nombre, codigo, precio, stock
            FROM productos
            ORDER BY LOWER(nombre) ASC, nombre ASC
        """
        with get_connection() as conn:
            rows = conn.execute(query).fetchall()

        return [
            {
                "nombre": row["nombre"],
                "codigo": row["codigo"],
                "precio": row["precio"],
                "stock": row["stock"],
            }
            for row in rows
        ]
