from typing import Any

from src.data.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository | None = None) -> None:
        self.repository = repository or ProductRepository()

    def create_product(self, data: dict[str, Any]) -> dict[str, Any]:
        nombre = self._required_text(data.get("nombre"), "nombre")
        codigo = self._required_non_negative_int(data.get("codigo"), "codigo")
        precio = self._required_non_negative_float(data.get("precio"), "precio")
        stock = self._required_non_negative_int(data.get("stock"), "stock")

        return self.repository.insert_product(
            nombre=nombre,
            codigo=codigo,
            precio=precio,
            stock=stock,
        )

    def get_products(self) -> list[dict[str, Any]]:
        return self.repository.list_products()

    @staticmethod
    def _required_text(value: Any, field_name: str) -> str:
        if value is None:
            raise ValueError(f"El campo '{field_name}' es obligatorio.")

        text_value = str(value).strip()
        if not text_value:
            raise ValueError(f"El campo '{field_name}' es obligatorio.")

        return text_value

    @staticmethod
    def _required_non_negative_int(value: Any, field_name: str) -> int:
        if value is None or str(value).strip() == "":
            raise ValueError(f"El campo '{field_name}' es obligatorio.")

        try:
            int_value = int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"El campo '{field_name}' debe ser numerico.") from exc

        if int_value < 0:
            raise ValueError(f"El campo '{field_name}' debe ser mayor o igual a 0.")

        return int_value

    @staticmethod
    def _required_non_negative_float(value: Any, field_name: str) -> float:
        if value is None or str(value).strip() == "":
            raise ValueError(f"El campo '{field_name}' es obligatorio.")

        try:
            float_value = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"El campo '{field_name}' debe ser numerico.") from exc

        if float_value < 0:
            raise ValueError(f"El campo '{field_name}' debe ser mayor o igual a 0.")

        return float_value
