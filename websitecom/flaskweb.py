from flask import Flask ,redirect, url_for , render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("homepage.html")

@app.route("/pat158-63")
def pat():
    return render_template("PAT1.html")

@app.route("/ข้อมูลการสมัครเข้าแต่ละมหาลัย")
def DataUc():
    return render_template("DataUc.html")

if __name__ == '__main__':
    app.run(debug=True)