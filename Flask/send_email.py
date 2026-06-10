from flask import Flask, render_template,request
from flask_mail import Mail, Message
from form import RegistrationForm

app = Flask(__name__)
app.secret_key = "sachinbelbase"

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "sachinbelbase818@gmail.com"  
app.config['MAIL_PASSWORD'] = "zpjw abie aozn pqem"
app.config['MAIL_DEFAULT_SENDER'] = "sachinbelbase818@gmail.com"

mail = Mail(app)

@app.route('/')
def home():
    return "Welcome!"

@app.route('/send-email', methods = ["GET", "POST"])
def send_email():
    form = RegistrationForm()
    if form.validate_on_submit():
        
        subject = form.subject.data
        recipients = form.recipients.data
        recipient_list = [r.strip() for r in recipients.split(",")]
        submit = form.submit.data
        
        msg = Message(
            subject=subject,
            recipients=recipient_list,
        )
        mail.send(msg)
        
        return (
            f"Email Sent Sucessfully <br><br>"
            f"Subject: {subject} <br><br>"
            f"Recipients: {recipients} <br> <br>" 
        )
        
    return render_template("send_email_with_UI.html",form = form)

    
if __name__ == '__main__':
    app.run(debug=True)
    
