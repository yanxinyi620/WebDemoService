from datetime import datetime
from flask import Flask, render_template, request, jsonify
from llm.llm_main import chat_response, format_response


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query')
def query():
    return render_template('query.html', 
                         title="查询模块",
                         description="在此进行查询操作")

@app.route('/chat')
def chat():
    return render_template('chat.html',
                         title="聊天模块",
                         description="在此进行聊天操作")

@app.route('/chat_api', methods=['POST'])
def chat_api():
    user_input = request.form.get('message')
    # 这里可以添加AI处理逻辑，示例使用简单回复

    chat_result = chat_response(query=user_input)
    output_json = format_response(chat_result)

    bot_response = f"AI：{output_json['response_content']}（当前时间：{datetime.now().strftime('%H:%M:%S')}）"

    return jsonify({
        'user': user_input,
        'bot': bot_response
    })

@app.route('/data')
def data():
    return render_template('data.html',
                         title="数据管理",
                         description="数据导入导出和管理")

@app.route('/report')
def report():
    return render_template('report.html',
                         title="报表生成",
                         description="生成并导出数据分析报告")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
