from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLACHEMY_DATABASE_URL"] = "sqlite:///temporadas.db"
app.config["SQLACHEY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class Temporada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_publicacao = db.Column(db.Date)
    status = db.Column(db.String(30), nullable=False)

class Episodio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temporada_id = db.Column(db.Integer, nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_publicacao = db.Column(db.Date)