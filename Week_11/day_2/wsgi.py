import flask

app = flask.Flask(__name__)


@app.route("/exercises")
def exercises():
    return flask.render_template('exercises.md')


@app.route("/lesson")
def lesson():
    return flask.render_template('in_this_chapter.md')


if __name__ == "__main__":
    app.run()
