from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from urllib.parse import urlparse
from app.url_shorter import URLShortener

bp = Blueprint('main', __name__)
url_shortener = URLShortener()

def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@bp.route("/<short_url>", methods=["GET"])
def redirect_to_url(short_url):
    original_url = url_shortener.expand(short_url)
    if original_url:
        return redirect(original_url)
    else:
        flash("Invalid URL")
        return redirect(url_for("main.index"))

@bp.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")
    if validate_url(original_url):
        short_url = url_shortener.shorten(original_url)
        return jsonify({'short_url': short_url}), 200
    else:
        return jsonify({'error': 'Invalid URL'}), 400