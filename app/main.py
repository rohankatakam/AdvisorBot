import os
from flask import Flask, render_template
from models import db

app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db.init_app(app)

@app.route("/") 
def home_view(): 
        return render_template('index.html')