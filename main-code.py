from flask import Flask, render_template
import requests
app = Flask(__name__)

# Sample product data (replace with a database or external source)
products = [
    {'id': 1, 'name': 'Awesome T-shirt', 'category': 'tshirts', 'image': 'tshirt1.jpg', 'price': 20},
    {'id': 2, 'name': 'Cool Cargo Pants', 'category': 'cargos', 'image': 'cargo1.jpg', 'price': 45},
    {'id': 3, 'name': 'Forea Shirt', 'category': 'forea shirts', 'image': 'forea1.jpg', 'price': 30},
    {'id': 4, 'name': 'Another T-shirt', 'category': 'tshirts', 'image': 'tshirt2.jpg', 'price': 22},
    {'id': 5, 'name': 'Stylish Cargos', 'category': 'cargos', 'image': 'cargo2.jpg', 'price': 50},
    {'id': 6, 'name': 'Forea Shirt Special', 'category': 'forea shirts', 'image': 'forea2.jpg', 'price': 35},
]

@app.route('/')
def home():
    # Prepare data for the template
    product_slides = products[:3]  # Example: First 3 products for the slider
    categories = ['forea shirts', 'tshirts', 'cargos']
    products_by_category = {}
    for category in categories:
        products_by_category[category] = [p for p in products if p['category'] == category]

    return render_template(
        requests.get('https://raw.githubusercontent.com/anonyyyyx/Website-Building-/refs/heads/main/home.html'),
        company_name="GLOGO",
        product_slides=product_slides,
        categories=categories,
        products_by_category=products_by_category
    )

if __name__ == '__main__':
    app.run(debug=True)
