from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('home/index.html')

@app.route("/home")
def home():
    return render_template('home/index.html')

@app.route("/admin")
def admin():
    return render_template('admin/index.html')

if __name__ == "__main__":
    app.run()