from flask import Blueprint, jsonify

bp = Blueprint("route", __name__)


@bp.route("/")
def home():
    response = {
        "message": "Hello World"
    }
    return jsonify(response)
