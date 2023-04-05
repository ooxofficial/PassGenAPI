from flask import Flask, render_template
import random

upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower = "qwertyuiopasdfghjklzxcvbnm"
numbers = "0123456789"
symbols = "!@#$%^&*()."
all = upper + lower + numbers + symbols
length = random.randint(8, 24)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", password="".join(random.sample(all, length)))

if __name__ == "__main__":
    app.run(debug=True)