# app.py
from flask import Flask, render_template, jsonify, request
from services import apply_decision

app = Flask(__name__)

@app.route('/')
def index():
    # Render the main game page
    return render_template('index.html')

@app.route('/game/start', methods=['GET'])
def game_start():
    # Initialize or reset the game state here
    return jsonify({'message': 'Game started successfully!'})

@app.route('/game/decision', methods=['POST'])
def game_decision():
    decision_data = request.json
    new_state = apply_decision(decision_data['decision'])
    return jsonify(new_state)

if __name__ == '__main__':
    app.run(debug=True)
