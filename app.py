from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'flask'
app.config['MYSQL_DATABASE_PASSWORD'] = 'monkey3110'
app.config['MYSQL_DATABASE_DB'] = 'flask'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
curror = conn.cursor()

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
        curror.callproc('createUser',(_name,_email,_password,_address,_phone))
        data = curror.fetchall()
        if len(data) is 0:
            conn.commit()
            return json.dumps({'html':'<span>User created successfully !!</span>'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()