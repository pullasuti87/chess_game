from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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


def pos_to_index(pos):
    row = 8 - int(pos[1])
    col = ord(pos[0]) - ord('a')
    return row, col


@app.route("/")
def home():
    return render_template("index.html", board=board, current_player="white")


@app.route("/move", methods=['POST'])
def move():
    global board

    from_row, from_col = pos_to_index(request.form['from_pos'])
    to_row, to_col = pos_to_index(request.form['to_pos'])

    piece = board[from_row][from_col]
    board[to_row][to_col] = piece
    board[from_row][from_col] = " "

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
