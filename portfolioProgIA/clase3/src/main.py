from flask import Flask, render_template

from src.api.product_routes import product_blueprint
from src.data.db import init_db


def create_app() -> Flask:
    flask_app = Flask(
        __name__,
        template_folder="frontend/templates",
        static_folder="frontend/static",
    )

    init_db()
    flask_app.register_blueprint(product_blueprint, url_prefix="/api")

    @flask_app.get("/")
    def home() -> str:
        return render_template("index.html")

    return flask_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
