from flask import Flask, render_template
#import web_scraping

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/stats')
def stats():
    return render_template("stats.html")


@app.route('/map')
def stats():
    return render_template("map.html")

if __name__ == "__main__":
 app.run(debug=True)