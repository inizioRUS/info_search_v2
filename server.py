from flask import Flask, render_template, request
from classes import Document
from search import  score, retrieve
from time import time

app = Flask(__name__, template_folder='.')


@app.route('/', methods=['GET'])
def index():
    start_time = time()
    query = request.args.get('query')
    if query is None:
        query = ''
    original, documents = retrieve(query)
    documents = sorted(documents, key=lambda doc: -score(original, doc[0]))
    results = [(*doc[1].format(), score(original, doc[0])) for doc in documents]
    return render_template(
        'index.html',
        time="%.2f" % (time() - start_time),
        query=query,
        search_engine_name='Yandex',
        results=results
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
