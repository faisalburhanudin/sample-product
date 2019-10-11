import logging

from flask import Blueprint, jsonify

bp = Blueprint("route", __name__)
log = logging.getLogger(__name__)


@bp.route("/")
def home():
    response = {
        "message": "Hello World"
    }
    return jsonify(response)


@bp.app_errorhandler(404)
def handling_notfound(e):
    log.warning(e)

    response = {
        "status": 404,
        "message": "endpoint not found"
    }
    return jsonify(response), 404


@bp.app_errorhandler(405)
def handling_method_error(e):
    log.warning(e)

    response = {
        "status": 404,
        "message": "method not allowed"
    }
    return jsonify(response), 404


@bp.app_errorhandler(500)
def handling_server_error(e):
    log.error(e)

    response = {
        "status": 404,
        "message": "internal server error"
    }
    return jsonify(response), 404