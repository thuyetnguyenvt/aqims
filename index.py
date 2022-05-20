from flask import render_template
from saleapp import app



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/test")
def test():
    return "WELCOME TO MY SITE!!!"

if __name__=="__main__":
    app.run(debug=True)

