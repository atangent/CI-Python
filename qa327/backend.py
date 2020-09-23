from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


def get_user(email):
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    user = User.query.filter_by(email=email).first()

    if user:
        return "User existed"

    if password != password2:
        return "The passwords do not match"

    if len(email) < 1:
        return "Email format error"

    if len(password) < 1:
        return "Password not strong enough"

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw)

    db.session.add(new_user)
    db.session.commit()
    return None
