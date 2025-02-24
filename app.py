from flask import Flask, render_template

app = Flask(__name__)


def init_board():
    # 8x8
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ]
    return board


@app.route("/")
def home():
    return render_template("index.html", board=init_board(), current_player="white")


@app.route("/move", methods=['POST'])
def move():
    return "HELLO"


if __name__ == "__main__":
    app.run(debug=True)
