import flask

app = flask.Flask(__name__)

users = ["Laurent", "Ally", "Angkush"]
articles = {'title': 'one Piece',
            'content': 'manga',
            'author': 'oda'}


@app.route("/blog")
def blog():
    return flask.render_template("homepage.html", users=users)


@app.route("/blog/articles")
def article():
    return flask.render_template("articles.html", articles=articles)


if __name__ == "__main__":
    app.run()