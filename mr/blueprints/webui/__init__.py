from flask import Blueprint

from .views import index, olympia

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index, endpoint="index")
bp.add_url_rule(
    "/olympia/<num>", view_func=olympia, endpoint="olympiaview"
)


def init_app(app):
    app.register_blueprint(bp)
