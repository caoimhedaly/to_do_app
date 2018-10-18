from flask import Flask, render_template

app = Flask(__name__)



t = [
    {
     'Todo': "Vacuum",
     'time': '10am'
    },
    {
     'Todo': "Wash floor",
     'time': '11am'
    }
    ]

@app.route("/")
def showHi():
    return render_template("index.html")





if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)