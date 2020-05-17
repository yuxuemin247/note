from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    print('1')
    abort(404)
    print('2')
    return 'test_abort'
@app.errorhandler(404)
def xxx(e):
    return 'xxx'
if __name__ == '__main__':
    app.run(debug=True)
