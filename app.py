from flask import Flask, request, render_template
from search_scraper import search_duckduckgo

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def hello_world():
    result = None
    if request.method == 'POST':
        word = request.form.get('word')
        result = search_duckduckgo(word)
    return render_template('index.html', data=result)


if __name__ == '__main__':
    app.run(debug=True)
