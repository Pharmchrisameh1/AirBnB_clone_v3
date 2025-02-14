#!/usr/bin/python3
""" API Module """


from flask import Flask, jsonify, make_response  # type: ignore
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS  # type: ignore


app = Flask(__name__)


app.register_blueprint(app_views, url_prefix='/api/v1')
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage session after every request.
    """
    storage.close()


@app.errorhandler(404)
def error_404(err):
    """Handler for the 404 error that returns a JSON.
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=int(port), threaded=True)
