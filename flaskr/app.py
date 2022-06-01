from flask import Flask, request, render_template
from markupsafe import escape
from flaskr import create_app

app = create_app()

@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/vowel_count", methods=['POST'])
def vowel_count():
    data = request.get_json()
    
    words = data['words']
    vowels = ['a','e','i','o','u']
    count = [len([v for v in word if v in vowels]) for word in words]
    
    result = dict(zip(words, count))
    
    return result

@app.route("/sort", methods=['POST'])
def sort():
    return "<p>Application is running with Flask!</p>"


if __name__ == "__main__":
    app.run(debug=True)