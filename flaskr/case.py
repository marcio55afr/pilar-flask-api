from flask import Blueprint, request, render_template
from markupsafe import escape
from . import create_app

bp = Blueprint('functions', __name__,)

@bp.route("/")
def home_page():
    return render_template('index.html')


@bp.route("/vowel_count", methods=['POST'])
def vowel_count():
    data = request.get_json()
    
    words = data['words']
    vowels = ['a','e','i','o','u']
    count = [len([v for v in word if v in vowels]) for word in words]
    
    result = dict(zip(words, count))
    
    return result


@bp.route("/sort", methods=['POST'])
def sort():
    return "<p>Application is running with Flask!</p>"