from .forms import Updateprofile,PostForm,Comment
from flask_login import login_required,current_user
from flask import render_template
from ..models import User,Post,Comment
from .. import db,photos
from . import main 
import datetime
from ..requests import get_quotes
import markdown2




@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''
  
  posts = Post.query.all()
  random = get_quotes()
  quote = random["quote"]
  quote_author = random["author"]
  title = "Blog"

  return render_template('index.html',posts = posts,random = random,quote_author = quote_author,title = title,quote = quote)



@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()
  # posts = Post.query.filter_by( post_id = uname).all()
  title = user.username.upper()
  if user is None:
      abort(404)

  return render_template("profile/profile.html",user = user, title = title)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)



@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))




       

@main.route('/<uname>/new/post', methods = ['GET','POST'])
@login_required
def new_post(uname):
    form = PostForm()
    user = User.query.filter_by(username = uname).first()
    

    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        
        
       
        new_post= Post()
        new_post.title = title
        new_post.post = post 
        new_post.author = current_user

             
        new_post.save_post()

        return redirect(url_for('main.single_post'))
        
        # posts = Post.query.all()
        

    return render_template("new_post.html",new_form = form)

@main.route("/<post_id>/comments")
@login_required
def view_comments(post_id):
    post = Post.query.filter_by(id = post_id).first()
    title = "Comments"
    comments = post.get_post_comments()

    return render_template("view_comment.html")


@main.route("/<user>/post/<post_id>/new/comment", methods = ["GET","POST"])
@login_required
def comment(user,post_id):
    user = User.query.filter_by(id = user ).first()
    post = Post.query.filter_by(id = post_id).first()
    form = Comment()
    title = "Add Comment"
    if form.validate_on_submit():
        content = form.content.data
        originalDate = datetime.datetime.now()
        
        new_comment = Comment(content = content, user = user, post = post)
        new_comment.save_comment()
        return redirect(url_for("main.comments", post_id= post.id))
    return render_template("comments.html,title = post.title,form = form, post = post ")

@main.route('/pitch/new/<int:id>')
def single_post(id):
    post=Post.query.get(id)
    if post is None:
        abort(404)
    
    return render_template('post.html',post = post )
