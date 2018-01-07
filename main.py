from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template ('/base.html')

@app.route("/validate", methods=["POST"])
def validate ():
    username=request.form['username']
    username_error=""
    password=request.form['password']
    password_error=""
    verify_password=request.form['verify_password']
    verify_password_error=""
    email_optional=request.form['email_optional']
    email_optional_error=""
    
    if (len(username) <=2 or len(username) >=20) or " " in username:
        username_error ="username error in length"
        
    if password != verify_password:
        verify_password_error = "password does not match"

    if email_optional != "" :
        if "@" not in email_optional  or "." not in email_optional:
            email_optional_error="email not correct"
        

    if username_error != "" or password_error != "" or verify_password_error !="" or email_optional_error != "":
        return render_template('/base.html',username_error=username_error,verify_password_error=verify_password_error,email_optional_error=email_optional_error,username=username,email_optional=email_optional) 
    
    else:
        return redirect("/welcome.html?username={0}".format(username))
    
  
@app.route("/welcome.html", methods=['GET'])
def hello ():
    username=request.args.get('username')
    return render_template("/welcome.html",username=username)

if __name__ == "__main__":
    app.run()