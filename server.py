from flask import Flask,render_template,url_for,redirect,request
from waitress import serve
import csv
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit_form', methods=['GET','POST'])
def submit():
    if request.method=="POST":
        try:
            data= request.form.to_dict()
            #print(data)
            write_data_csv(data)
            message='form submitted,we will get in touch to you shortly'
            return render_template("thankyou.html",message=message)
        except:
            message="DID NOT SAVED DATA  TO DATABASE"
            return render_template("thankyou.html",message=message)
    else:
        message= "FORM NOT SUBMITTED"
        return render_template("thankyou.html",message=message)
    
@app.route('/about.html')
def about():
    return render_template("about.html")
@app.route('/contact.html')
def contactt():
    return render_template("contact.html")


def write_data_csv(data):
    name=data['name']
    email=data['email']
    password=data['password']
    message=data['message']
    
    with open("db.csv",'a') as csvfile:
        #f.write("name: {}, email: {}, password: {}, message: {}".format(name,email,password,message))
         db_writer =csv.writer(csvfile, delimiter=",",quotechar="|",quoting=csv.QUOTE_MINIMAL)
         db_writer.writerow([name,email,password,message])
         
mode="dev"         
if __name__ == "__main__":
    
    if mode=="dev":
        app.run(host='0.0.0.0',port=50100, debug=True)
    else:
         serve(app, host='0.0.0.0',port=50100, threads=2)
       
    # app.run(debug=True)