from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    a = request.form.get('a', 'default')
    return 'Hello, {}!'.format(a)

if __name__ == '__main__':
    app.run()
