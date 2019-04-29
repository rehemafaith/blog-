from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager 




class Quotes:
  '''
  Quotes class to define Quotes Objects 
  '''

  def __init__(self,id,author,title,description,urlToImage,url):

      self.id = id
      self.author = author 
      self.quote = quote

class User(UserMixin,db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String,unique = True,index=True)
  pass_secure = db.Column(db.String)


  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)


  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)


  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))

  def __repr__(self):
    return f'User {self.username}'
    

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key= True)
    content = db.Column(db.String)
    title = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship("Comment", backref = "pitch", lazy = "dynamic")
    category = db.Column(db.String)

    
    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_post(cls,id):
        posts = Post.query.filter_by(post_id=id).first()
        comments = Comment.query.filter_by(post_id = post.id).order_by(Comment.time.desc())
        return posts


class Comment(db.Model):
    
    __tablename__= "comments"

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer,db.ForeignKey("posts.id"))

    def save_comment(self):
        db.session.ass(self)
        db.session.commmit()
     
    


