# 🌸 CMC GLOW – E-commerce Beauty & Skincare

An online store built with Django for selling authentic Korean skincare products. This project was developed as part of the Advanced Programming (PA) laboratory at the Faculty of Automation, Computers and Electronics (FACE), University of Craiova.

An online store built with Django for selling authentic Korean skincare products.  
It includes user authentication, shopping cart, wishlist, order history, Stripe card payments, and Sameday delivery.

---

## 🔑 Features
- 👤 User Registration and Login: Users can create accounts and log in securely.
- 🔐 Secure Authentication: Password hashing and session management for user security.
- 🛒 Shopping Cart: Add or remove products with dynamic quantity updates.
- ❤️ Wishlist: Save favorite products for future reference.
- 💳 Checkout with Stripe: Secure card payments via Stripe API.
- 🧾 Order History: View past orders with details.
- 🚚 Sameday Delivery Integration: Delivery options powered by Sameday API.
- 📝 Blog/Articles System: Optional feature for skincare tips and product guides.

⚠️ Known Issues and Limitations
- Payment Processing: Stripe payments are in test mode and do not process real transactions.
- Sameday API: Limited to specific regions; may require additional configuration for full functionality.
- Blog System: Partially implemented; lacks advanced features like commenting or categorization.
- Mobile Responsiveness: Some frontend elements may not be fully optimized for mobile devices.
- Database: SQLite is used for simplicity, which may not be suitable for production-scale traffic.

---

## 🧪 Technologies Used
- Backend: Python, Django
- Frontend: HTML, CSS
- Database: SQLite 
- Payments: Stripe API
- Delivery: Sameday API

---

## 📦 Requirements

To run this project locally, install the dependencies:

```
pip install -r requirements.txt
🔧 Setup Instructions
Clone the repository:

Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate  # On Windows
Install dependencies:

pip install -r requirements.txt
Apply migrations and run the server:

python manage.py migrate
python manage.py runserver
Open in browser:
http://127.0.0.1:8000

📁 Project Structure
Beauty-Skincare/
├── accounts/            # User authentication and profiles
├── media/              # Uploaded media files
├── products/           # Product and cart logic
├── screenshots/        # Screenshots for README
├── skincare_store/     # Django project settings
├── static/             # CSS, JS, and images
│   └── images/
├── templates/          # HTML templates
├── venv/               # Virtual environment
├── manage.py           # Django management script
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation

## 📸 Screenshots

### 🏠 Home
![Home](https://github.com/cataacraciun/E-commerce_BeautySkincare/blob/main/screenshots/home.png?raw=true)

### ❤️ Wishlist
![Wishlist](https://github.com/cataacraciun/E-commerce_BeautySkincare/blob/main/screenshots/wishlist.png?raw=true)

### 🛒 Cart
![Cart](https://github.com/cataacraciun/E-commerce_BeautySkincare/blob/main/screenshots/cart.png?raw=true)

### 👤 Account
![Account](https://github.com/cataacraciun/E-commerce_BeautySkincare/blob/main/screenshots/account.png?raw=true)

### 🔓 Logout
![Logout](https://github.com/cataacraciun/E-commerce_BeautySkincare/blob/main/screenshots/logout.png?raw=true)

### 📬 Contact
![Contact](https://github.com/cataacraciun/E-commerce_BeautySkincare/blob/main/screenshots/contact.png?raw=true)

📜 Disclaimer

This project is the result of the Advanced Programming (PA) laboratory at the Faculty of Automation, Computers and Electronics (FACE), University of Craiova (http://ace.ucv.ro/). It is intended for educational purposes and may contain limitations or incomplete features. Use it at your own risk, and ensure proper configuration for any production environment.
