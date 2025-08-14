from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        email = request.form['email']
        return f"Received: {username}, {email}"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
