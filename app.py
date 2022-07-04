from flask import Flask,render_template,request
import instaloader


app = Flask(__name__)

@app.route('/')
def instagram():
   return render_template("index.html")

@app.route('/download',methods=["GET","POST"])
def  download_insta():
    ig = instaloader.Instaloader()
    db = request.form.get("insta")

    ig.download_profile(db,profile_pic_only=True)
    return "Success"

if __name__=="__main__":
    app.run()
