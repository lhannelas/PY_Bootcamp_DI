import flask

app = flask.Flask(__name__)


@app.route("/index")
def index():
    return flask.render_template("index.html")


@app.route("/index/blue")
def blue():
    return flask.render_template("blue.html")


@app.route("/index/yellow")
def yellow():
    return flask.render_template("yellow.html")


@app.route("/index/green")
def green():
    return flask.render_template("green.html")


@app.route("/index/red")
def red():
    return flask.render_template("red.html")


if __name__ == "__main__":
    app.run(port=8080)
