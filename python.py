
from flask import Flask,render_template,request,redirect
from recognition_system import rec_img
from PIL import Image
import io
import os
import base64
from werkzeug.utils import secure_filename
app=Flask(__name__)
app.config["IMAGE_UPLOADS"]="C:\\LSM_Project\\SPARK-main\\uploads"
filename=''
@app.route("/home",methods=['GET','POST'])
def upload_image():
    if request.method=="POST":
        image= request.files['file']
        if image.filename=='':
            print("Image must have a file name")
            return redirect(request.url)
        filename=secure_filename(image.filename)
        basedir=os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename))
        img=Image.open(app.config["IMAGE_UPLOADS"]+"/"+filename)
        list1=rec_img(app.config["IMAGE_UPLOADS"]+"/"+filename)
        
        if list1==-1:
            return  render_template("index.html",flag=-1)
        if list1==-2:
            return render_template("index.html",flag1=-1)
        data=io.BytesIO()
        img.save(data,"JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())
        if list1!=[]:
         return render_template("index.html", filename=encoded_img_data.decode('utf-8'),
                               plate=list1[0],
                               name=list1[1],
                               licenseno=list1[2],
                               address=list1[3],
                               ph=list1[4],
                               warning=list1[5],
                               fine=list1[6])
    return render_template("index.html")

app.run(debug=True, port=5001)

