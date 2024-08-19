from flask import Flask, render_template, request, session, redirect, url_for
import requests, random
from words import words
from hangman_art import stages, logo


app = Flask(__name__)
app.secret_key = "test_environment"


def get_random_word():
    return random.choice(words).upper()


@app.route('/')
def index():
    if "word" not in session:
        session["word"] = get_random_word()
        session["guesses"] = []
        session["misses"] = 0
        session["message"] = ""
        session["current_stage"] = stages[0]
    word_display = "".join([letter if letter in session["guesses"] else "_" for letter in session["word"]])
    return render_template('index.html', word_display=word_display, guesses= session["guesses"], misses= session["misses"], message=session.get("message", ""), word=session["word"], current_stage=session["current_stage"], logo=logo)


@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for("index"))


@app.route('/guess', methods=["POST"])
def guess():
    guess = request.form["guess"].upper()
    if guess not in session["guesses"]:
        session["guesses"].append(guess)
        if guess in session["word"]:
            session["message"] = f"Well done '{guess}' is in the word"
        else:
            session["misses"] += 1
            session["current_stage"] = stages[session["misses"]]
            session["message"] = f"Wrong '{guess}' is NOT in the word"
    else:
        session["message"] = f"You already guessed '{guess}'."
    return redirect(url_for('index'))
        




if __name__ == "__main__":
    app.run(debug=True)