from flask import Flask, render_template, make_response, url_for, redirect, request, session
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '2abbb6cbe9bf31ad2459b1e51783b7f741f589b0'
#app.permanent_session_lifetime Время жизни сессии 31 день
app.permanent_session_lifetime = datetime.timedelta(days=10)

@app.route("/")
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1 #обновление данных сессии
    else:
        session['visits'] = 1 #запись данных в сессию
    return f"<h1>Main Page</h1><p>Число просмотров: {session['visits']}"

data = [1,2,3,4]
@app.route("/session")
def session_data():
    session.permanent = True
    if 'data' not in session:
        session['data'] = data
    else:
        session['data'][1] += 1
        session.modified = True

    return f"<p>session['data']: {session['data']}"

if __name__ == "__main__":
    app.run(debug=True)