import json
from GPT_USE import *
from flask import Flask, jsonify, request
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

# @app.route('/testpsy',methods=['GET'])
# def test():
#     return jsonify({"code": 200, "message": "success", "data": ''})

if __name__ == '__main__':

    ip='0.0.0.0'
    port = 2023
    app.run(ip, port, debug=False)