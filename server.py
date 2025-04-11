from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求（前后端分离时需要）

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    # 这里可以接 ChatGPT、LLM、数据库、你自己的逻辑
    reply = f"你刚才说的是：『{user_msg}』，我收到啦！"
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(port=5000)
