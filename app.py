from flask import Flask, escape, request, render_template
from forsearch import searchreq
import json
import os
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search', methods=['POST'])
def search():
    """if POST, query movie api for data and return results."""
    title=request.form['title']
    jsonresp=searchreq(title)
    results=jsonresp["Search"]
    return render_template("search_results.html",results=results)

@app.errorhandler(404)
def notfound(error):
    return render_template('notfound.html'),404


if __name__=="__main__":
    app.run(debug=True)


'''
@app.route('/favorites')
def favorites():
    #Read out favorited movies.
    filename = os.path.join('data.json')
    with open(filename) as data_file:
        data = json.load(data_file)
        return data

@app.route('/favoritess')
def favoritess():
    #if query params are passed, write movie to json file
    return render_template('favorites.html')


@app.route('/movie/<movie_oid>')
def movie_detail():
    """if fetch data from movie database by oid and display info."""
    qs_name = request.args.get('name', '')
    qs_oid = request.args.get('oid', '')
    return 'Hello, {escape(name)}!'

'''
