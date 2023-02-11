from flask import Flask, request, render_template
from Model.DbHandler import DbHandler
import os
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


@app.route('/riderSignUp', methods=["GET", "POST"])
def riderSignUp():
    if request.method == "POST":
        username = request.form["riderName"]
        useremail = request.form["riderEmail"]
        password = request.form["riderPassword"]
        cnic = request.form["riderCnic"]
        phoneNo = request.form["riderPhoneNo"]
        licenseFile = request.files["riderLicense"]
        CriminalRecFile = request.files["riderCriminalRec"]
        licenseFilename = licenseFile.filename
        CriminalRecFilename = CriminalRecFile.filename
        licenseFile.save(os.path.join('/static/License/licenseFile/', licenseFilename))
        CriminalRecFile.save(os.path.join('/static/CriminalRecord/CriminalRecFile/', CriminalRecFilename))

        # if licenseFile:
        #     licenseFile.save(licenseFile.filename)
        #     licenseFile.save(os.path.join('../static/License/licenseFile/', licenseFilename))
        #     print ("file Saved")
        # else:
        #     print ("File not found")
        #
        # if CriminalRecFile:
        #     CriminalRecFile.save(CriminalRecFile.filename)
        #     CriminalRecFile.save(os.path.join('../static/CriminalRecord/CriminalRecFile/', CriminalRecFilename))
        #     print("file Saved")
        # else:
        #     CriminalRecFilename = ""
        #     print("No Criminal Record")

        handler = makeHandler()
        handler.riderSignup(username, useremail, password, cnic, phoneNo, licenseFilename, CriminalRecFilename)
    return render_template("riderSignUp.html")

if __name__ == '__main__':
    app.run()
