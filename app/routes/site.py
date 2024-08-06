from flask import render_template, Blueprint


dp = Blueprint("site", __name__)


@dp.route("/")
@dp.route("/portfolio")
def portfolio():
    return render_template("index.html")


@dp.route('/portfolio-detail')
def portfolio_detail():
    return render_template("/portfolio-details.html")


@dp.route("/service-detail")
def service_detail():
    return render_template("/service-details.html")


@dp.route("/starter-page")
def starter_page():
    return render_template("/starter-page.html")

