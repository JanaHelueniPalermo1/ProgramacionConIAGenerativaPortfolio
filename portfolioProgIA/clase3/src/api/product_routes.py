from flask import Blueprint, jsonify, request

from src.business.product_service import ProductService

product_blueprint = Blueprint("product_blueprint", __name__)
service = ProductService()


@product_blueprint.get("/health")
def health() -> tuple[dict[str, str], int]:
    return {"status": "ok"}, 200


@product_blueprint.post("/productos")
def create_product():
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Debes enviar un JSON valido."}), 400

    try:
        created = service.create_product(payload)
        return jsonify(created), 201
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


@product_blueprint.get("/productos")
def get_products():
    products = service.get_products()
    return jsonify(products), 200
