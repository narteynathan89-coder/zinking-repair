from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    phone = request.form['phone']
    issue = request.form['issue']
    with open('bookings.txt', 'a') as f:
        f.write(f"{name}, {phone}, {issue}\n")
    return f"<div style='font-family:Arial; text-align:center; padding:50px;'><h1>✅ Thanks {name}!</h1><p>We received: {issue}</p><p>We go call you on <b>{phone}</b> soon.</p><a href='/'>Go Back Home</a><br><br><a href='https://wa.me/233533834097'>Chat WhatsApp 0533834097</a></div>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)