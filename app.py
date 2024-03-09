from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'johanna.chambers92@gmail.com'
app.config['MAIL_PASSWORD'] = 'hapo jfhc aqpq mlbz '
app.config['MAIL_DEFAULT_SENDER'] = 'johanna.chambers92@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('frontpage.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Sending confirmation email to the user
        msg_to_user = Message('Thank you for your message!', recipients=[email])
        msg_to_user.body = f"Hello {name},\n\nThank you for contacting me. I have received your message and will get back to you soon.\n\nBest regards,\n Johanna Chambers"
        mail.send(msg_to_user)

        # Sending notification email to you as the recipient
        msg_to_me = Message('New Contact Form Submission', recipients=['johanna.chambers92@gmail.com'])
        msg_to_me.body = f"You have received a new message from {name} ({email}):\n\n{message}"
        mail.send(msg_to_me)

        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/skills')
def skills():
    return render_template('skills.html')
if __name__ == '__main__':
    app.run(debug=True)
