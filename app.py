#from Game_of_life import GameOfLife

from flask import Flask, render_template, request
from game_of_life import GameOfLife



app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/live')
def live():
    game = GameOfLife()
    '''
    if game.counter == 0:
        width = int(request.form["width"])
        height = int(request.form["height"])
        GameOfLife(width, height)
    '''
    matr = game.world
    old_world = game.old_world
    game.form_new_generation()
    game.counter += 1
    return render_template("live.html", matr=matr, counter=game.counter, old_world=old_world)

@app.route("/process", methods=["POST"])
def process():
    width = int(request.form["width"])
    height = int(request.form["height"])
    game = GameOfLife(width, height)
    return render_template("process.html")


if __name__=='__main__':
    app.run(debug=True)
  