import logging

from flask import Blueprint, jsonify, request

from app import user

bp = Blueprint("route", __name__)
log = logging.getLogger(__name__)


class RequestError(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code


@bp.route("/")
def home():
    response = {
        "message": "Hello World"
    }
    return jsonify(response)


@bp.route("/user", methods=["POST"])
def create_user():
    """Create User endpoint"""
    username = request.form.get("username")
    email = request.form.get("email")

    if not username and not email:
        raise RequestError("missing username and email")

    usr = user.create(username=username, email=email)

    response = {
        "id": usr.id,
        "username": usr.username,
        "email": usr.email,
        "photo": usr.photo_url,
        "clothes_size": usr.clothes_size
    }

    return jsonify(response)


@bp.route("/user/<user_id>")
def get_user(user_id):
    """Get user by id"""
    usr = user.get_by_id(user_id)

    response = {
        "id": usr.id,
        "username": usr.username,
        "email": usr.email,
        "photo": usr.photo_url,
        "clothes_size": usr.clothes_size
    }

    return jsonify(response)


@bp.route("/user/<user_id>", methods=["delete"])
def delete_user(user_id):
    """Delete user by id"""
    user.delete(user_id)

    response = {
        "message": "delete success"
    }

    return jsonify(response)


@bp.app_errorhandler(RequestError)
def handling_request_error(e):
    log.warning(e)
    response = {
        "message": e.message
    }
    return jsonify(response), e.status_code


@bp.app_errorhandler(404)
def handling_notfound(e):
    log.warning(e)
    response = {
        "message": "endpoint not found"
    }
    return jsonify(response), 404


@bp.app_errorhandler(405)
def handling_method_error(e):
    log.warning(e)
    response = {
        "message": "method not allowed"
    }
    return jsonify(response), 405


@bp.app_errorhandler(500)
def handling_server_error(e):
    log.error(e)
    response = {
        "message": "internal server error"
    }
    return jsonify(response), 500
