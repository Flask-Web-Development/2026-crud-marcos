from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///temporadas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Temporada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_publicacao = db.Column(db.Date)
    status = db.Column(db.String(30), nullable=False)

    episodios = db.relationship(
        "Episodio",
        backref="temporada",
        lazy=True
    )


class Episodio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_publicacao = db.Column(db.Date)

    temporada_id = db.Column(
        db.Integer,
        db.ForeignKey("temporada.id"),
        nullable=False
    )


@app.route("/temporadas/cadastrar", methods=["GET", "POST"])
def cadastrar_temporada():

    if request.method == "POST":
        temporada = Temporada(
            titulo=request.form["titulo"],
            descricao=request.form["descricao"],
            data_publicacao=datetime.strptime(
                request.form["data_publicacao"],
                "%Y-%m-%d"
            ).date(),
            status=request.form["status"]
        )

        db.session.add(temporada)
        db.session.commit()

        return "Temporada cadastrada com sucesso!"

    return render_template("cadastrar_temporada.html")


@app.route("/episodio/cadastrar", methods=["GET", "POST"])
def cadastrar_episodio():

    if request.method == "POST":
        episodio = Episodio(
            numero=request.form["numero"],
            titulo=request.form["titulo"],
            descricao=request.form["descricao"],
            data_publicacao=datetime.strptime(
                request.form["data_publicacao"],
                "%Y-%m-%d"
            ).date(),
            temporada_id=request.form["temporada_id"]
        )

        db.session.add(episodio)
        db.session.commit()

        return "Episodio cadastrado com sucesso!"

    temporadas = Temporada.query.all()

    return render_template(
        "cadastrar_episodio.html",
        temporadas=temporadas
    )


@app.route("/temporada/editar/<int:id>", methods=["GET", "POST"])
def editar_temporada(id):

    temporada = Temporada.query.get_or_404(id)

    if request.method == "POST":
        temporada.titulo = request.form["titulo"]
        temporada.descricao = request.form["descricao"]
        temporada.data_publicacao = datetime.strptime(
            request.form["data_publicacao"],
            "%Y-%m-%d"
        ).date()
        temporada.status = request.form["status"]

        db.session.commit()

        return "Temporada editada com sucesso!"

    return render_template(
        "editar_temporada.html",
        temporada=temporada
    )


@app.route("/episodio/editar/<int:id>", methods=["GET", "POST"])
def editar_episodio(id):

    episodio = Episodio.query.get_or_404(id)

    if request.method == "POST":
        episodio.numero = request.form["numero"]
        episodio.titulo = request.form["titulo"]
        episodio.descricao = request.form["descricao"]
        episodio.data_publicacao = datetime.strptime(
            request.form["data_publicacao"],
            "%Y-%m-%d"
        ).date()
        episodio.temporada_id = request.form["temporada_id"]

        db.session.commit()

        return "Episodio editado com sucesso!"

    temporadas = Temporada.query.all()

    return render_template(
        "editar_episodio.html",
        episodio=episodio,
        temporadas=temporadas
    )


@app.route("/temporadas")
def listar_temporadas():
    temporadas = Temporada.query.all()

    return render_template(
        "temporadas.html",
        temporadas=temporadas
    )


@app.route("/episodios")
def listar_episodios():
    episodios = Episodio.query.all()

    return render_template(
        "episodios.html",
        episodios=episodios
    )


@app.route("/temporadas/excluir/<int:id>", methods=["POST"])
def excluir_temporada(id):
    temporada = Temporada.query.get_or_404(id)

    db.session.delete(temporada)
    db.session.commit()

    return redirect(url_for("listar_temporadas"))


@app.route("/episodio/excluir/<int:id>", methods=["POST"])
def excluir_episodio(id):
    episodio = Episodio.query.get_or_404(id)

    db.session.delete(episodio)
    db.session.commit()

    return redirect(url_for("listar_episodios"))


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)