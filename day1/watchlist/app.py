from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
import click
import os
import sys


WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"      #windows平台
else:
    prefix = "sqlite:////"      #Mac.Linux平台

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = prefix + os.path.join(app.root_path,'data.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# 数据层
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


@app.route('/')
def index():
    return render_template("index.html")


# 自定义命令
@app.cli.command()
@click.option("--drop",is_flag = True,help = "先删除再创建")
def initdb(drop):
    if drop:
        db.create_all
    db.create_all()
    click.echo("数据库初始完成")