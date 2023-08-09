from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index/<name>/<group>")
def view_home(name, group):
    return render_template("index.html", name=name, group=group)


@app.route("/home")
def new_home():
    return render_template("home.html", title="Home")


@app.route("/fruits")
def fruit():
    fruits = ["apples", "banana", "cherry", "fig"]
    return render_template("fruit_list.html", title="Fruits", fruits=fruits)


@app.route("/about_us")
def about_us():
    return render_template("about_us.html", title="About Us")


if __name__ == "__main__":
    app.run()
