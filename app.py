from flask import Flask, request, render_template
from Model.DbHandler import DbHandler
app = Flask(__name__)


def makeHandler():
    return DbHandler(host="localhost", username="root", password="", db="road2door")

@app.route('/adminSignIn', methods=["GET", "POST"])
def adminSignIn():  # put application's code here
    if request.method == "POST":
        username = request.form["adEmail"]
        password = request.form["adPassword"]

        handler = makeHandler()

        if handler.checkUserExist(username, password, "admin"):   # hardcode value (option)
            return "Login Successful"
        else:
            return render_template("adminSignIn.html", error="Invalid username or password.")
    return render_template("adminSignIn.html")


if __name__ == '__main__':
    app.run()
