# # Guess a number between 0 and 9
from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media2.giphy.com/media/UIpzEC5QTvuOQ/giphy.webp?cid' \
           '=ecf05e47j7l4e0mdbycj4qf7anuq3udjpxq27ytgrdtdcg8h&rid=giphy.webp"/> '


random_num = random.randint(0, 9)
print(random_num)


@app.route('/<number>')
def check_num(number):
    num = int(number)
    if num < random_num:
        output = "<h1 style='color:red'>Too Low, Try again!</h1>" \
                 "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif num > random_num:
        output = "<h1 style='color:purple'>Too high, Try again!</h1>" \
                 "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        output = "<h1 style='color:green'>You found me!</h1>" \
                 "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

    return output


if __name__ == "__main__":
    app.run(debug=True)
