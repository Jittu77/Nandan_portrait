from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

# Route for the Home Page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Route for the About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the Blog Page
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Route for the Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the Detail Page
@app.route('/detail')
def detail():
    return render_template('detail.html')

# Route for the Service Page
@app.route('/service')
def service():
    return render_template('service.html')

# Route for the Team Page
@app.route('/team')
def team():
    return render_template('team.html')

# Route for the Testimonial Page
@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

# Route to handle form submission and send message to WhatsApp
@app.route('/send_whatsapp', methods=['POST'])
def send_whatsapp():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Format the message to be sent to WhatsApp
        whatsapp_number = "7325060600"  # Replace with your WhatsApp Business number
        whatsapp_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        # URL encode the message
        whatsapp_message = urllib.parse.quote(whatsapp_message)

        # Create the WhatsApp URL
        whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"

        # Redirect to WhatsApp with the pre-filled message
        return redirect(whatsapp_url)

if __name__ == '__main__':
    app.run(debug=True)
