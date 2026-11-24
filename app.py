from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my app, u are going to be jomokers!"

@app .route("/about")
def about():
    return "About jmk48."

@app.route("/user/<name>")
def profile(name):
    return f"Whats up Niggas {name}."

@app.route("/post/<int:id>")
def post(post_id):
    return f"Post #{post_id}."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name")
    if not name:
        return "Please provide a name."
    return f"Hallo, {name}! selamat datang di web jomok"

if __name__ == "__main__":
    app.run(debug=True)