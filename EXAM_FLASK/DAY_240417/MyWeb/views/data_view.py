## --------------------------------------------------------
## 역할 : 데이터 저장 및 출력관련 웹 페이지 라우팅 처리
## URL : /input
##       /input/save
##       /input/delete
##       /input/update
## --------------------------------------------------------
## 모듈 로딩
from flask import Blueprint, render_template, request
import datetime
import os

## BP 인스턴스 생성
data_BP = Blueprint('data',
                    __name__, 
                    template_folder='templates',
                    url_prefix='/input')            # 중요!

MODE = 'POST'

## 라우팅 함수들
## http://127.0.0.1:5000/input/
@data_BP.route('/')
def input_data():
    return render_template('input_data.html', 
                           action='/input/save', method=MODE)

## GET 방식으로 데이터 저장 처리 함수
## 사용자의 요청. 즉, request 객체에 데이터 저장되어 있음
@data_BP.route('/save_get')
## http://127.0.0.1:5000/input/save_get
def save_get_data():
    # 요청 데이터 추출
    req_dict = request.args.to_dict()
    # return f"SAVE GET DATA: {req_dict}"
    # v = req_dict.get('value')
    # m = req_dict.get('message')
    # return render_template('save_data.html', value=v, message=m)
    return render_template('save_data.html', **req_dict)

## POST 방식으로 데이터 저장 처리
@data_BP.route('/save_post', methods=['POST'])
## http://127.0.0.1:5000/input/save_post
def save_post_data():
    # 요청 데이터 추출
    method = request.method
    headers = request.headers
    args = request.args.to_dict()   # 왜 없지??
    v = request.form['value']
    m = request.form['message']
    return f"SAVE POST DATA =><br>\METHOD : {method}<br>HEADERS : {headers}<br>\
        ARGS : {args}<br>value : {v}<br>message : {m}"

@data_BP.route('/save', methods=['GET', 'POST'])
## http://127.0.0.1:5000/input/save
def save_data():
    html_result=""
    
    if MODE == 'GET':
        args = request.args.to_dict()
        return f"SAVE DATA => <br>value : {args.get('value')}<br>message : {args.get('message')}"
    if MODE == 'POST':
        v = request.form['value']
        m = request.form['message']
        if 'img_file' in request.files:
            img_ = request.files['img_file'] # 이미지 객체 저장 (터미널 경로 기준)
            img_filename = img_.filename
            prefix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
            save_path = f'./MyWeb/static/img/{prefix}_{img_filename}'
            # return f'{os.getcwd()}'
            img_.save(save_path)            # 서버 경로에 이미지 저장
            html_result += f"<img src={f'../static/img/{prefix}_{img_filename}'} style='width: 500px;'><br>"  # html 파일 기준
        html_result += f"SAVE DATA => <br>value : {v}<br>message : {m}"
        return html_result


@data_BP.route('/update', methods=['GET', 'POST'])
## http://127.0.0.1:5000/input/update
def upload_img():
    pass