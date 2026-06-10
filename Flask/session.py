from flask import Flask, session, render_template
from flask_mail import Message

app = Flask(__name__)

app.secret_key = "Sachin Belbase"

#### Setting Session Data ####
@app.route('/login')
def login():
    session['username'] = 'Sachin'
    return "Logged in!"


#### Accessing Session Data ####
@app.route('/profile')
def profile():
    username = session.get('username')
    return f"Logged in as {username}"


#### Removing Session Data ####
@app.route('/logout')
def logout():
    session.pop('username', None)
    return "Logged out!"


@app.route('/')
def home():
    return render_template("cookies.html")

if __name__ =='__main__':
    app.run(debug=True)
    