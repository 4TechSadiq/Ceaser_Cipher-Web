from flask import render_template, Flask, request, redirect
from cipher import *
app = Flask(__name__, template_folder="public", static_folder="static")


@app.route("/",methods=["POST","GET"])
def home():
    print(request.method)
    if request.method == "POST":
        message = request.form.get("message")
        enc = request.form.get("enc")
        dec = request.form.get("dec")
        print(message,enc,dec)
        
        result = None
        
        if enc != None:
           result =  caesar(start_text=message, shift_amount = 7, cipher_direction="Encode")
           print(result)
        elif dec != None:
           result = caesar(start_text=message, shift_amount = 7, cipher_direction="Decode")
        return render_template("index.html", msg = result)

    return render_template("index.html",msg="Output Shows Here")



if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=80, use_reloader=True, threaded=True,debug=False)
