from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://example.sqlite"
db = SQLAlchemy(app)

@app.route("/") 
def home_view(): 
        return render_template('index.html')