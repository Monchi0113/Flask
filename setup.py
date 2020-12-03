from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def megane():
    return render_template('index.html')
#  kiyopage.htmlを読み込む為のコード
if __name__ == "__main__":
    app.run()
