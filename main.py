import json
from GPT_USE import *
from flask import Flask, jsonify, request
from gevent import pywsgi
app = Flask(__name__)

@app.route('/GPT_conversation',methods=['POST'])
def GPT_conversation():
    global e
    try:
        e=None
        q_data = request.get_data()
        q_dict = json.loads(q_data) 
        conversation= q_dict["conversation"]
        model=q_dict['model']
        result=ask_conversation(conversation,model)

        if result!=False:
            return jsonify({"code": 200, "message": "success", "data": result})
        else:
            return jsonify({"code": 500, "message": 'failed', "data": result})
    except Exception as e:
        return jsonify({"code": 500, "message": str(e), "data": None})

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0',80),app)
    server.serve_forever()