import flask

# from flask import render_template_string


app = flask.Flask(__name__)

users = ["bob", "alice"]
articles = ["article1", "article2"]
article = {'title': 'one Piece',
           'content': 'manga',
           'author': 'oda'}


# @app.route("/")
# def index():
#     return "Hello World"
#
#
# @app.route("/blog")
# def wellcomeUsers():
#     return f"Hello {users}"
#
#
# @app.route("/blog/articles")
# def displayArticles():
#     return articles
#
#
#
# @app.route("/sayHi/<name>")
# def sayHello(name):
#     template = '''
#     <html>
# 	    <head>
# 	        <title>Home Page - Microblog</title>
# 	    </head>
# 	    <body>
# 	        <h1>Hello, {{username}}!</h1>
# 	    </body>
# 	</html>'''
#
#     return flask.render_template_string(template, username=name)

@app.route("/blog/")
def blog():
    return flask.render_template('homepage.html', name=users)


@app.route("/blog/articles")
def articles():
    return flask.render_template('articles.html', article=article)

@app.route("/profile")
def profile():
    return flask.redirect(flask.url_for("blog"))

if __name__ == "__main__":
    app.run(port=8080)
