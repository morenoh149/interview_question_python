from flask import Flask, escape, request, render_template, url_for
import json,os
import urllib.request as request
app = Flask(__name__)

api_key = "4c2d5800"
base_url = "http://img.omdbapi.com/?apikey=[apikey]&"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorites')
def favorites():
#    Read out favorited movies.
    filename = os.path.join('data.json')
    with open(filename) as data_file:
        data = json.load(data_file)
        return data

@app.route('/search', methods=['POST'])
def search(movie_name):
    """if POST, query movie api for data and return results."""
#    query = request.form['title']
#    return f'Hello, {query}'


@app.route('/movie/<movie_oid>')
def movie_detail():
    """if fetch data from movie database by oid and display info."""
    qs_name = request.args.get('name', '')
    qs_oid = request.args.get('oid', '')
    return f'Hello, {escape(name)}'


@app.errorhandler(404)
def notfound(error):
    return render_template('notfound.html'),404

if __name__ == '__main__':
    app.run(debug = True,port = 5000)

'''
@app.route('/favorites')
def favorites():
    """if query params are passed, write movie to json file."""
    return render_template('favorites.html')


@app.route('/movie/<movie_oid>')
def movie_detail():
    """if fetch data from movie database by oid and display info."""
    qs_name = request.args.get('name', '')
    qs_oid = request.args.get('oid', '')
    return f'Hello, {escape(name)}!'
'''
