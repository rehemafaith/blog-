from flask_mail import Message 
from flask import render_template 
from . import mail 

def mail_message(subject,template,to,**kwargs):
  

  email = Message(subject, sender = "rehemafaith01@gmail.com",recipients=[to])
  email.body = render_template(template + ".txt",**kwargs)
  
  mail.send(email)