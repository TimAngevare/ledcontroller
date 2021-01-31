import flask
import board
import controller

app = flask.Flask(__name__)

@app.route("/",  methods=["POST","GET"])
def index():
    if flask.request.method == "POST":
        if "nm" in flask.request.form:
            h = flask.request.form["nm"].lstrip("#")
            controller.setcolor(tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))
        elif "fill" in flask.request.form:
            controller.fill()
        elif "slide" in flask.request.form:
            controller.slide()

        return flask.render_template("template.html", quote="I love you")
    else:
       return flask.render_template("template.html", quote="I love you")
    
if __name__ == "__main__":
    app.run(debug=True,  host="0.0.0.0")