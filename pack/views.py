from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, current_user
from . import db 
LoginManager = LoginManager()

views = Blueprint('views', __name__, template_folder='public')

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    from .db_custom import FormQue
    form = FormQue.query.filter_by(user=current_user.id).all()

    useragent = request.headers.get('User-Agent')
    ipaddr = request.headers.get('X-Forwarded-For', request.remote_addr)

    return render_template('home.html', user=current_user, form=form, useragent=useragent, ipaddress=ipaddr) 

@views.route('/nojs')
def nojs():
    return render_template('nojs.html')


@views.route('/form/<shorturl>', methods=['GET', 'POST'])
def formanswer(shorturl):
    from .db_custom import FormQue
    form = FormQue.query.filter_by(shorturl=shorturl).first()

    if form is None:
        return redirect(url_for('views.error'))

    questions = {}
    for i in range(1, 11): 
        question = getattr(form, f'question{i}', None)
        if question:
            questions[f'question{i}'] = question

    if request.method == 'POST':
        user = form.user
        name = request.form.get('name')
        email = request.form.get('email')
        answers = {}

        for i in range(1, 11):
            answer = request.form.get(f'answer{i}')
            if answer:
                answers[f'answer{i}'] = answer

        from .db_custom import FormAns
        new_answer = FormAns(user=user, name=name, email=email, shorturl=shorturl, **answers)
        db.session.add(new_answer)
        db.session.commit()
        return redirect(url_for('views.home'))

    return render_template('answerform.html', form=form, questions=questions)

@views.route('/form/<shorturl>/answers')
@login_required
def formanswers(shorturl):
    user = current_user.id
    from .db_custom import FormAns, FormQue
    answers = FormAns.query.filter_by(shorturl=shorturl).all()
    question = FormQue.query.filter_by(shorturl=shorturl).first()
    
    if not answers:
        return render_template('viewans.html', x=question, message="No answers yet")

    user_has_answered = any(int(answer.user) == int(user) for answer in answers)
    if not user_has_answered:
        return redirect(url_for('views.error'))

    questions = [getattr(question, f'question{i}', None) for i in range(1, 11)]

    processed_answers = []
    for ans in answers:
        processed_answers.append({
            'name': ans.name,
            'email': ans.email,
            'date': ans.date,
            **{f'answer{i}': getattr(ans, f'answer{i}', None) for i in range(1, 11)}
        })

    return render_template(
        'viewans.html',
        x=question,
        questions=questions,
        answers=processed_answers,
        message=None
    )



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