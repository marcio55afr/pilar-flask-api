from flask import Blueprint, request, render_template, abort

bp = Blueprint('functions', __name__)

@bp.route("/")
def home_page():
    return render_template('index.html')


@bp.route("/vowel_count", methods=['POST'])
def vowel_count():
    data = request.get_json()
    if ('words' not in data.keys()):
        # A required key is missing from the received json.
        abort(400)
    
    words = data['words']
    try:
        words_iter = iter(words)
    except TypeError as e:
        # The values are not within an iterable object
        abort(400)
    
    non_string_values = [type(w)!=str for w in words_iter]
    if (any(non_string_values)):
        #The values type from the received json are not expected.
        abort(400)
    
    vowels = ['a','e','i','o','u']
    vowels_count = [len([v for v in word if v in vowels]) for word in words]
    
    result = dict(zip(words, vowels_count))
    
    return result


@bp.route("/sort", methods=['POST'])
def sort():
    return "<p>Application is running with Flask!</p>"