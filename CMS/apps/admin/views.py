
from flask import Blueprint

bp = Blueprint("admin", __name__)


@bp.route("/admin")
def index():
    return "this is end-index"
