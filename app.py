from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'   # was SQLACLCHEMY (typo)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False           # was SQLACHEMY (typo)

db = SQLAlchemy(app)

# Model (table)
class Car(db.Model):
    id    = db.Column(db.Integer, primary_key=True)   # Column not column, Integer not Intger, primary_key not Primary_Key
    name  = db.Column(db.String(100))                 # String not string
    price = db.Column(db.String(50))

# Create DB + Add sample data
with app.app_context():                # @before_first_request was removed in Flask 3.x, this is the modern way
    db.create_all()

    if not Car.query.first():
        car1 = Car(name="BMW M3", price="R90000")
        car2 = Car(name="BMW X5", price="R120000")
        car3 = Car(name="BMW i8", price="R2500000")

        db.session.add_all([car1, car2, car3])
        db.session.commit()

# Routes
@app.route("/")        # was @app.rout (missing e)
def index():
    cars = Car.query.all()
    return render_template('index.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)