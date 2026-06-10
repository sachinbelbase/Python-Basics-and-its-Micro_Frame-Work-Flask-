from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
        
    recipients = StringField(
        label="Recipients: ", description="Enter your receptiance with ( , ) separated",
        validators=[DataRequired()]
        
    )
    
    subject = StringField(
        label="Subject: ", description="Enter the Subject",
        validators=[Length(min=1,max=1000)]
        
    )
    
    body = StringField(
        label="Message: ", description="Write the message you want to send",
        validators=[Length(min=1,max=1000)]
        
    )
    
    submit = SubmitField("Send Mail: ", description="Send the mail")

# class NameForm(FlaskForm):
#     name = StringField("Enter Your Name: ", validators=[DataRequired()])
#     submit = SubmitField("Submit")

# class RegistrationForm(FlaskForm):
#     name = StringField(
#         "Full Name",
#         validators=[DataRequired()]
        
#     )
    
#     email = StringField(
#         "Email",
#         validators=[DataRequired(), Email()]
        
#     )
    
#     password = PasswordField(
#         "Password",
#         validators=[DataRequired()]  
#     )
    
#     gender = RadioField(
#         "Gender",
#         choices=[
#         ("M", "Male"),
#         ("F", "Female")
#         ]
#     )
    
#     country = SelectField(
#         "Country",
#         choices=[
#         ("np", "Nepal"),
#         ("in", "India")
#         ]
#     )
    
#     agree = BooleanField(
#         "I accept all the terms and conditions",
#         validators=[DataRequired()]
#     )
#     submit = SubmitField("Register")