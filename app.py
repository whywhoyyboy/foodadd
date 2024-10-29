from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("global_page.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/menu')
def menu():
    return  render_template("menu.html")

if __name__ == '__main__':
    app.run(debug=True)