### 파일명이 __init__.py라 Flask run 시 자동으로 실행된다.
### 왜냐하면 바깥 .env의 FLASK_APP = MyWeb 폴더로 설정되어 있기 때문에.

## 모듈 로딩
from flask import Flask, render_template, url_for

### Application Factory 기반의 Flask Server 구동
### 함수명 : create_app 변경 불가
### 반환값 : Flask Server 인스턴스 (Flask 모듈이 갖게 됨)
def create_app():
    ## Flask Server 인스턴스 생성
    app = Flask(__name__)

    ## Blueprint 인스턴스 등록 : 서브 카테고리에 해당하는 페이지 라우팅 기능
    # app.register_blueprint()
    @app.route('/')
    def index():
        # return '<h1>hello</h1>'
        return render_template('index.html')    # html 파일은 templates 안에서 찾도록 정해져 있음

    # 데이터 전송하는 라우팅 => 변수<타입:변수명>
    @app.route('/user/<name>')
    def user_info(name):
        # return f"<h1>hello{name}</h1>"
        return render_template('index.html', name=name)

    # 테스트 기능
    with app.test_request_context():
        print(f"url_for 경로 : {url_for(endpoint='static', filename='style_1.css')}")

    ## Flask Server 인스턴스 반환
    return app