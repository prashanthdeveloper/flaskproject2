from flask import Flask,render_template,redirect,request


app=Flask(__name__)



@app.route('/',methods=["GET","POST"])
def index():
    if request.method=='GET':

        return render_template('index.html')

    if request.method=="POST":
        username=request.form.get("uname")
        password=request.form.get('passw')

        if password=="im_prashanth":

            return  'Login succesfully'
        else:
            return "Incorrect password"


# @app.route("/send_email",methods=["GET","POST"])
# def send_email():
#     try:
#         msg = Message('Hello from the other side!', sender = "prashanthsonu94@gmail.com", recipients = ["prashanthsonu94@gmail.com"])
#         msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
#         mail.send(msg)
#         return "Message sent!"
#     except Exception as e:
#         raise e
#         pass

if __name__=="__main__":
    app.run(debug=True)
