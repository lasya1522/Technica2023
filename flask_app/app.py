from flask import Flask, render_template
import web_scraping

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")