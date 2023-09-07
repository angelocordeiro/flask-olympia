from flask import abort, render_template
from mr.models import Mrdata


def index():
    olympias = Mrdata.query.all()
    return render_template("index.html", olympias=olympias)


def olympia(num):
    olympia = Mrdata.query.filter_by(num=num).first() or abort(
        404, "O nao encontrado"
    )
    return render_template("olympia.html", olympia=olympia)
