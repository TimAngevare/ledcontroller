import flask
import board
#import bot
import controller
import bot
from random import randint

app = flask.Flask(__name__)

def choose():
    quotes = ["I love you", "you're cute", "My lover", "I need you", "I love you more", "Hey gorgeous",  "Hey beautifull", "Looking good!", "You're loved", "Mwah", "Hey bby"]
    return quotes[randint(0, len(quotes) - 1)]

@app.route("/",  methods=["POST","GET"])

def index():
    if flask.request.method == "POST":
        if "nm" in flask.request.form:
            h = flask.request.form["nm"].lstrip("#")
            brightness = flask.request.form["slider"]
            controller.setcolor(tuple(int(h[i:i+2], 16) for i in (0, 2, 4)), int(brightness))
        elif "fill" in flask.request.form:
            controller.gone()
            controller.fill()
        elif "stack" in flask.request.form:
            controller.gone()
            controller.stack()
        elif "pulse" in flask.request.form:
            controller.gone()
            controller.pulser()
        elif "slide" in flask.request.form:
            controller.gone()
            controller.slide()

        return flask.render_template("template.html", quote=choose())
    else:
       return flask.render_template("template.html", quote=choose())
    
if __name__ == "__main__":
    app.run(debug=True,  host="0.0.0.0", port=80)
