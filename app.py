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
    try:
        if request.method == "POST":
            print("in post method")
            rider_name = request.form['riderName']
            rider_email = request.form['riderEmail']
            rider_password = request.form['riderPassword']
            rider_cnic = request.form['riderCnic']
            rider_phone_no = request.form['riderPhoneNo']
            license = request.files['riderLicense']
            criminal_record = request.files['riderCriminalRec']

            license.save('./static/License/license' + ' '+ license.filename)
            criminal_record.save('./static/CriminalRecord/criminal_record' +' '+ criminal_record.filename)

            # save the uploaded files to the desired location
            # license.save(os.path.join('/static/License', license.filename))
            # criminal_record.save(os.path.join('/static/CriminalRecord', criminal_record.filename))

            # # get the file paths
            # rider_license_path = os.path.join('/static/License', license.filename)
            # rider_criminal_record_path = os.path.join('/static/CriminalRecord', license.filename)


            # insert the data into the database
            handler = makeHandler()
            handler.Signup(rider_name, rider_email, rider_password, rider_cnic, rider_phone_no, license.filename,
                           criminal_record.filename)

        return render_template("riderSignUp.html")

    except Exception as e:
        print("Error: ", e)
        return "error"

if __name__ == '__main__':
    app.run(debug=True)
