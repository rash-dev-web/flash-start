from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/hello_world')
@make_bold
@make_emphasis
@make_underline
def hello_world():
    return 'World!'


if __name__ == "__main__":
    app.run(debug=True)
