from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game

@app.route('/roshambo')
def index():
    return render_template('index.html', title='New Game') 

@app.route('/roshambo', methods=['POST'])
def play_game():
    name1 = request.form['name1']
    weapon1 = request.form['weapon1']
    name2 = request.form['name2']
    weapon2 = request.form['weapon2']
    result = Player.roshambo(name1, weapon1, name2, weapon2)
    return render_template('result.html', title = "Good Game", result = result, name1 = name1, name2 = name2, weapon1 = weapon1, weapon2 = weapon2)

@app.route('/roshambo/scissors/rock')
def sr():
    return f"Player 2 wins with Rock"

@app.route('/roshambo/scissors/paper')
def sp():
    return f"Player 1 wins with Paper"

@app.route('/roshambo/scissors/scissors')
def ss():
    return f"It's a draw!"

@app.route('/roshambo/rock/scissors')
def rs():
    return f"Player 1 wins with Rock"

@app.route('/roshambo/rock/paper')
def rp():
    return f"Player 2 wins with Paper"

@app.route('/roshambo/rock/rock')
def rr():
    return f"It's a draw"

@app.route('/roshambo/paper/scissors')
def ps():
    return f"Player 2 wins with Scissors"

@app.route('/roshambo/paper/rock')
def pr():
    return f"Player 1 wins with Paper"

@app.route('/roshambo/paper/paper')
def pp():
    return f"It's a draw"