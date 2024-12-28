from flask import Flask, send_from_directory, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/about')
def about():
    return send_from_directory('.', 'about.html')

@app.route('/blog')
def blog():
    return send_from_directory('.', 'blog.html')

@app.route('/cart')
def cart():
    return send_from_directory('.', 'cart.html')

@app.route('/contact')
def contact():
    return send_from_directory('.', 'contact.html')

@app.route('/shop')
def shop():
    return send_from_directory('.', 'shop.html')

@app.route('/sproduct')
def sproduct():
    return send_from_directory('.', 'sproduct.html')


@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)


@app.route('/api/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Product A", "price": 100, "description": "High-quality product A"},
        {"id": 2, "name": "Product B", "price": 150, "description": "Durable product B"},
        {"id": 3, "name": "Product C", "price": 200, "description": "Affordable product C"}
    ]
    return jsonify(products)


@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username == 'admin' and password == 'password':
        return jsonify({"message": "Login successful", "status": "success"})
    return jsonify({"message": "Invalid credentials", "status": "fail"})

if __name__ == '__main__':
    app.run(debug=True)
