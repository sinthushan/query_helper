from flask import Flask, render_template
import json
from screen import Mvest

app = Flask(__name__)


@app.route("/")
def hello_world():
    screens = mvest.screens
    return render_template('index.html', screens = screens)

@app.route("/<screen>")
def query_screen(screen):
    mvest.set_current_screen(screen)
    return render_template('screen.html', screen = mvest.current_screen) 


if __name__ == "__main__":
    with open('mvest.json') as f:
        json_file = json.load(f)
    mvest = Mvest(**json_file)
    app.run(debug=True)