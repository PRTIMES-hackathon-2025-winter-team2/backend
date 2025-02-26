from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# サンプルデータ
todos = [
    {"id": 1, "title": "買い物に行く", "completed": False},
    {"id": 2, "title": "メールを確認する", "completed": True}
]

# GETリクエスト: すべてのTODOを取得
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# POSTリクエスト: 新しいTODOを追加
@app.route('/api/todos', methods=['POST'])
def add_todo():
    new_todo = request.json
    new_todo['id'] = len(todos) + 1
    todos.append(new_todo)
    return jsonify(new_todo), 201

# 特定のTODOを取得
@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Todo API!"})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
