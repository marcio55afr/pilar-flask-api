from flask import Blueprint, request, render_template, abort, jsonify
from flaskr.case_validation import valid_string_list, valid_order_param

bp = Blueprint('functions', __name__)


@bp.route("/")
def home_page():
    return render_template('index.html')


@bp.route("/vowel_count", methods=['POST'])
def vowel_count():
    data = request.get_json()
    
    if (not valid_string_list(data, 'words')):
        # Input data is unacceptable
        abort(400)
    
    words = data['words']
    vowels = ['a','e','i','o','u']
    vowels_count = [len([v for v in word if v in vowels]) for word in words]
    
    result = dict(zip(words, vowels_count))
    
    return result


@bp.route("/sort", methods=['POST'])
def sort():
    data = request.get_json()
    
    if (not valid_string_list(data, 'words') or
        not valid_order_param(data, 'order')):
        # Input data is unacceptable
        abort(400)
    
    words = data['words']
    reverse = data['order'] == 'desc'
    
    return jsonify(sorted(words, reverse=reverse))
