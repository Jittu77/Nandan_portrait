from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
