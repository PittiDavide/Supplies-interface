from flask import Flask, send_from_directory

app = Flask(__name__)

# Path for our main Svelte page


@app.route("/")
def base():
    return send_from_directory('../frontend/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)


@app.route("/<path:path>")
def home(path):
    return send_from_directory('../frontend/public', path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
