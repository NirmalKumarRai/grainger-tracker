from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class ProductResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    url = db.Column(db.String(1000))
    price = db.Column(db.String(255))
    image_url = db.Column(db.String(1000))
    mpn = db.Column(db.String(255))
    specification_1 = db.Column(db.Text)  # Adjust as needed
    specification_2 = db.Column(db.Text)  # Adjust as needed
    datasheets = db.Column(db.String(1000))  # Adjust as needed
    product_description = db.Column(db.Text)  # Adjust as needed
    accessories = db.Column(db.Text)  # Adjust as needed
    scraped_by = db.Column(db.String(255))

    def __repr__(self):
        return f"ProductResult(name={self.name}, price={self.price}, url={self.url}, ...)"

# Add more models as needed for other entities in your database
