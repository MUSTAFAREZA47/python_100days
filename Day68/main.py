from flask import Flask, render_template, redirect, url_for, request, flash, send_file, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime, os

# -------------------- Setup --------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB init
db = SQLAlchemy(app)

# -------------------- Models --------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# -------------------- Forms --------------------
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

# -------------------- Routes --------------------
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=16)
        print(hashed_pw)
        new_user = User(username=form.username.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash("User registered successfully! Please login.", "success")
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            token = jwt.encode({
                'user': user.username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, app.config['SECRET_KEY'], algorithm="HS256")
            session['jwt_token'] = token
            return redirect(url_for('secret'))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html", form=form)

@app.route('/secret')
def secret():
    token = session.get('jwt_token')
    if not token:
        flash("Please log in first", "warning")
        return redirect(url_for('login'))
    try:
        jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    except:
        flash("Session expired, please log in again", "danger")
        return redirect(url_for('login'))

    return render_template("secret.html")

@app.route('/download')
def download():
    token = session.get('jwt_token')
    if not token:
        return redirect(url_for('login'))
    try:
        jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return send_file("secret.pdf", as_attachment=True)
    except:
        return redirect(url_for('login'))


# -------------------- Run --------------------
if __name__ == '__main__':
    if not os.path.exists('users.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
