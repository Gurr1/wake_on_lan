from flask import Flask, request, render_template
import os

app = Flask(__name__)

password = "test" # TODO Change this
mac_address = "\"8C:89:A5:C1:EC:EF\""

@app.route("/poweron", methods=['POST', 'GET'])
def powerOn():
    if request.method == 'POST':
        request_password = request.form['password']
        if request_password == password:
            os.execv("wakeonlan " + mac_address)
    else:
        return render_template("password_input.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)
