### 모둘 로딩
from flask import Blueprint, render_template, request, redirect
from YouWeb.models import Question              # 터미널 실행경로 기준
from YouWeb import db   # __init__.py 안의 SQLAlchemy 객체(db) 불러옴

### BP 인스턴스 생성
bp = Blueprint(name='main', import_name=__name__, 
               template_folder='templates', url_prefix='/')

### 라우팅 함수들
@bp.route('/')
def index(): 
    ## Question 테이블에 저장된 데이터 읽어서 출력
    question_list = Question.query.order_by(Question.create_date.desc())    # question 내용 저장
    return render_template('question/question_list.html', question_list=question_list)
    # return f"<h3>HI {question_list}</h3>"

@bp.route('/question/create')
def enter_information():
    # Question 테이블에 데이터 입력하기
    return render_template('question/question_create.html')

@bp.route('question/save', methods=['GET', 'POST'])
def save_information():
    # 입력된 정보를 받아서 보여주고, DB에 저장하는 페이지
    subject, content, create_date = request.form['subject'], request.form['content'], request.form['create_date']
    if content and subject:
        question = Question(subject=subject, content=content)
        db.session.add(question)    # db에 추가
        db.session.commit()                 # db에 적용
    return redirect("/")
    # return f'{id}, {subject}, {content}, {create_date}'
