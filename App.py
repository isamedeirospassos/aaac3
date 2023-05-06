from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/users')
def get_users():
    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
        {"id": 3, "name": "Bob"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)