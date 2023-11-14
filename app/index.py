from flask import render_template, request, redirect, url_for
import dao
from app import app
from app import login
from flask_login import login_user, logout_user


@app.route('/admin/login', methods=['post'])
def user_login():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            user = dao.check_user(username=username, password=password)

            if user:
                login_user(user=user)
                return redirect(url_for('home'))


@app.route('/admin/logout', methods=['post'])
def user_logout():
    logout_user()
    return redirect('/admin')


@app.route("/")
def home():
    kw = request.args.get('kw')
    cates = dao.load_catgories()
    product = dao.load_products(kw)
    return render_template('index.html', catgories=cates, products=product)


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin

    app.run(debug=True)
