from .forms import Updateprofile,PostForm,Comment
from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Post,Comment
from .. import db,photos
from . import main 
import datetime





@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''
  posts = Post.query.all()
  title = "Blog"
  return render_template('index.html', title = title, posts = posts)
# @main.route('/pitch/pitch/new/<int:id>') # , methods = ['GET','POST'])
# @login_required
# def new_pitch(id):


@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()
  posts = Post.query.filter_by(username = uname).order_by(Post.time.desc())
  title = user.name.upper()
  if user is None:
      abort(404)

  return render_template("profile/profile.html",posts = posts,user = user, title = title)


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
    title = "Edit Profile"
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



       

@main.route('/<uname>/new/pitch', methods = ['GET','POST'])
@login_required
def new_post(uname):
    form = PostForm()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    title1 = "New Post"

    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        
        originalDate = datetime.datetime.now()
        time = str(originalDate.time())
        time =time[0:5]
        date = str(originalDate)
        date = date[0:10]
        new_post= Post(title= title, post = post,category= category,user = current_user, date = date, time = time)

        new_post.save_pitch()
        posts = Post.query.all()
        return redirect(url_for("main.submit",category = category))

    return render_template("new_post.html",new_form = form, title = title1)

@main.route("/<post_id>/comments")
@login_required
def view_comments(post_id):
    post = Post.query.filter_by(id = post_id).first()
    title = "Comments"
    comments = post.get_post_comments()

    return render_template("view_comment.html",comments = comments, post = post, title = title)

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
        time = str(originalDate.time())
        time = time[0:5]
        date = str(originalDate)
        date = date[0:10]
        new_comment = Comment(content = content, user = user, post = post)
        new_comment.save_comment()
        return redirect(url_for("main.comments", post_id= post.id))
    return render_template("comments.html,title = post.title,form = form, post = post ")

# @main.route('/pitch/<int:id>')
# def single_pitch(id):
#     pitch=Pitch.query.get(id)
#     if pitch is None:
#         abort(404)
#     
#     return render_template('pitch.html',pitch = pitch,format_pitch=formart_pitch)
@main.route("/post/<category>")
def categories(category):
    post = None
    if category == "all":
        posts = Post.query.order_by(Post.time.desc())

    else:
        posts = Post.query.filter_by(category = category).order_by(Post.time.desc()).all()


    return render_template("post.html",posts = posts, title = category.upper())
