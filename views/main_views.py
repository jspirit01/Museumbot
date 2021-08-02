from flask import Blueprint, render_template, request

bp = Blueprint('bp', __name__)

## GET 방식으로 값을 전달받음.
## num이라는 이름을 가진 integer variable를 넘겨받는다고 생각하면 됨.
## 아무 값도 넘겨받지 않는 경우도 있으므로 비어 있는 url도 함께 mapping해주는 것이 필요함
@bp.route('/')
def main_get():
    return render_template('test.html')

@bp.route('/calculate', methods=['POST', 'GET'])
def calculate():
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        #temp = request.form['num']
        pass
    elif request.method == 'GET':
        ## 넘겨받은 질문
        temp = request.args.get('question')
        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        return render_template('test.html', question=temp)
    ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함
