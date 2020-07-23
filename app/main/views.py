from flask import request,render_template,abort ,session, redirect, url_for,flash,current_app
from flask_login import login_required,current_user
from .forms import EditProfileForm,EditProfileAdminForm,SearchForm
from ..models import User,Role,Permission, Article
from .scrape import get_story_dawn,get_story_express,get_story_thenews,get_story_dependent,get_text
from .import main
from .. import db
from ..decorators import admin_required


@main.route('/',methods={'GET','POST'})
def index():
    form = SearchForm()
    if current_user.can(Permission.SEARCH) and form.validate_on_submit():
        print(form.news_site.data)
        if form.news_site.data == "5":
            get_text(form.news_url.data,current_user)
        if form.news_site.data == "4":
            get_story_dependent(form.news_url.data,current_user)    
        if form.news_site.data == "3":
            get_story_express(form.news_url.data,current_user)
        if form.news_site.data  == "2":
            get_story_dawn(form.news_url.data,current_user)
            print('This should be printed')
        if form.news_site.data  == "1":
            get_story_thenews(form.news_url.data,current_user)
        return redirect(url_for('.index'))
    page = request.args.get('page',1,type=int)
    pagination = Article.query.order_by(Article.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False
    )
    articles = pagination.items
    return render_template('index.html',form=form,articles=articles,pagination=pagination)



@main.route('/edit-profile',methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated')
        return redirect(url_for('.user',username=current_user.username))
    form.name.data = current_user.name  
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html',form=form)


@main.route('/edit-profile/<int:id>',methods=['GET','POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        flash('The Profile has been updated')
        return redirect(url_for('.user',username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html',form=form,user=user)


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = user.articles.order_by(Article.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    articles = pagination.items
    return render_template('user.html', user=user, articles=articles,
                           pagination=pagination)