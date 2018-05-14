from flask import Flask
from flask import render_template
from flask import request
from lib import naropy


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    narou = naropy.Naropy()
    if request.method == 'POST':
        user_id = request.form['user_id']
        bookmark_id = request.form['bookmark_id']
        print("post")

        return render_template('ranking.html',
                               user_id=user_id, bookmark_id=bookmark_id)
    else:
        return render_template('ranking.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

# http://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4
# http://jinja.pocoo.org/docs/dev/
# http://tnakamura.hatenablog.com/entry/20101214/flask
# http://python-remrin.hatenadiary.jp/entry/2017/05/01/152455
