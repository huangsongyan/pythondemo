#encoding:utf-8

from flask import Flask
from flask import request
import json

app =  Flask(__name__)

#支持post json请求
@app.route('/json',methods=['POST'])
def my_json():
    print request.headers['Content-Type']
    header = request.headers['Content-Type']
   # json.dumps(request.json)
    print request.json
    return 'hello'

if __name__ == '__main__':
    app.run(port=8080)


