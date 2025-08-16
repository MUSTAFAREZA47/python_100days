from flask import Flask, render_template, redirect, url_for
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # Required for CSRF protection

@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Here you could save to database, send email, etc.
        name = form.name.data
        email = form.email.data
        message = form.message.data
        return redirect(url_for('success', name=name))
    return render_template('contact.html', form=form)

@app.route('/success/<name>')
def success(name):
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
