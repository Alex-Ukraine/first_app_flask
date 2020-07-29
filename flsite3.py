from flask import Flask, render_template, make_response, url_for, redirect

app = Flask(__name__)

menu = [{"title": "Главная", "url": "/"},
        {"title": "Добавить статью", "url": "/add_post"}]

@app.route("/")
def index():
    # content = render_template('index.html', menu=menu, posts=[])
    # res = make_response(content)
    # img = None
    # with app.open_resource( app.root_path + "/static/images/ava.png", mode="rb") as f:
    #     img = f.read()
    # if img is None:
    #     return "None image"
    # res = make_response(img)
    # res.headers['Content-Type'] = 'text/plain'
    # res.headers['Content-Type'] = 'image/png'
    # res.headers['Server'] = 'flasksite'
    # res = make_response("<h1>Ошибка сервера</h1>", 500)
    # return res
    return "<h1>Main Page</h1>", 200, {'Content-Type': 'text/plain'}

@app.errorhandler(404)
def pageNot(error):
    return("Страница не найдена", 404)

@app.route('/transfer')
def transfer():
    return redirect(url_for('index'), 301)

@app.before_first_request
def before_first_request():
    print("before_first_request() called")

@app.before_request
def before_request():
    print("before_request() called")

@app.after_request
def after_first_request(response):
    print("after_request() called")
    return response

@app.teardown_request
def teardown_request(response):
    print("teardown_request() called")
    return response



if __name__ == "__main__":
    app.run(debug=True)