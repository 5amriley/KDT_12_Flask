### 모듈 로딩
from flask import Flask, render_template

### 전역변수
langapp = Flask(__name__)   # flask run 으로 실행되면 __name__ : EU_LANG_WEB.eu_lang_app

# ### 실행 제어
# if __name__ == '__main__':
#     # import 된 것이 아니고, 직접 실행됐을때만
#     # Flask 웹 서버 구동
#     print('이건 실행됨')
#     langapp=Flask('EU_LANG_WEB.eu_lang_app')
#     langapp.run(debug=True)   # --debug 옵션으로 flask run하면, 코드 수정한 결과를 새로고침하면 바로 볼 수 있다.

# 왜 if __name__ == '__main__'이 발동되면 이 함수가 실행 안 되는 거지?
### 웹 서버의 첫 페이지 : http://127.0.0.1:5000/ <=> /
@langapp.route('/')
def index_page():
    # return "<h3><font color='green'>My Web Index Page</font></h3>"
    return render_template('input_template.html')
