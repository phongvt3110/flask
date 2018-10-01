from flask import Flask, render_template, request, json
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

@app.route("/signUp", methods=['POST'])
def signup():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _address = request.form['inputAddress']
    _phone  = request.form['inputPhone']
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
    return render_template('admin/index.html')

if __name__ == "__main__":
    app.run()