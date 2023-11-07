from flask import render_template, request
import dao
from app import app


@app.route("/")
def home():
    kw=request.args.get('kw')
    cates = dao.load_catgories()
    product = dao.load_products(kw)
    return render_template('index.html', catgories=cates, products=product)


if __name__ == '__main__':
    app.run(debug=True)
