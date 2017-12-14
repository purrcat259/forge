from flask import Flask, render_template

app = Flask(__name__)


def run():
    print(render_template('blog.html', blog_text='This is my text'))

with app.app_context():
    run()
