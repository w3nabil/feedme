from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, current_user
from .db_custom import User
from . import db 
LoginManager = LoginManager()

views = Blueprint('views', __name__, template_folder='public')

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    from .db_custom import FormQue
    form = FormQue.query.filter_by(user=current_user.id).all()
    return render_template('home.html', user=current_user, form=form) 

@views.route('/nojs')
def nojs():
    return render_template('nojs.html')


@views.route('/form/<shorturl>', methods=['GET', 'POST'])
def formanswer(shorturl):
    from .db_custom import FormQue
    form = FormQue.query.filter_by(shorturl=shorturl).first() or None

    if form is None :
        return redirect(url_for('views.error'))

    if request.method == 'POST':
        shorturl = shorturl
        user = form.user
        name = request.form.get('name')
        email = request.form.get('email')
        answer1 = request.form.get('answer1' or None)
        answer2 = request.form.get('answer2' or None)
        answer3 = request.form.get('answer3' or None)
        answer4 = request.form.get('answer4' or None)
        answer5 = request.form.get('answer5' or None)
        answer6 = request.form.get('answer6' or None)
        answer7 = request.form.get('answer7' or None)
        answer8 = request.form.get('answer8' or None)
        answer9 = request.form.get('answer9' or None)
        answer10 = request.form.get('answer10' or None)
        from .db_custom import FormAns
        new_answer = FormAns(user=user, name=name, email=email, answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5, answer6=answer6, answer7=answer7, answer8=answer8, answer9=answer9, answer10=answer10, shorturl=shorturl)
        db.session.add(new_answer)
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template('answerform.html', form=form)

@views.route('/form/<shorturl>/answers')
@login_required
def formanswers(shorturl):
    user = current_user.id
    from .db_custom import FormAns, FormQue
    answer = FormAns.query.filter_by(shorturl=shorturl).all()
    question = FormQue.query.filter_by(shorturl=shorturl).first() 

    for i in answer:
        if int(i.user) == int(user):
            print("no error")
            return render_template('viewans.html', i=answer, x=question)
        else:
            return redirect(url_for('views.error'))

@views.route('/makeform', methods=['GET', 'POST'])
@login_required
def makeform():
    if request.method == 'POST':
        title = request.form.get('title' or None)
        description = request.form.get('description' or None)
        question1 = request.form.get('question1' or None)
        question2 = request.form.get('question2' or None)
        question3 = request.form.get('question3' or None)
        question4 = request.form.get('question4' or None)
        question5 = request.form.get('question5' or None)
        question6 = request.form.get('question6' or None)
        question7 = request.form.get('question7' or None)
        question8 = request.form.get('question8' or None)
        question9 = request.form.get('question9' or None)
        question10 = request.form.get('question10' or None)
        user = current_user.id

        from random import choice

        def shorturl():
            characters = '0123456789'
            shorturl = ''.join(choice(characters) for x in range(8))
            return shorturl
        
        shorturl = shorturl()

        with open('shorturl.txt', 'r') as file:
            shorturls = file.read().splitlines()

        while shorturl in shorturls:
            shorturl = shorturl()
        
        with open('shorturl.txt', 'a') as file:
            file.write(shorturl + '\n')

        from .db_custom import FormQue
        new_form = FormQue(title=title, shorturl=shorturl, description=description, question1=question1, question2=question2, question3=question3, question4=question4, question5=question5, question6=question6, question7=question7, question8=question8, question9=question9, question10=question10, user=user)
        db.session.add(new_form)
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template('makeform.html', user=current_user)

@views.route('/error')
def error():
    return render_template('error.html')