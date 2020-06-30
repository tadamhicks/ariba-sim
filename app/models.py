from datetime import datetime
from app import app, db
from sqlalchemy.exc import IntegrityError

class RequestItems(db.Model):
    __tablename__ = 'request'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2000), nullable=False)
    morpheus_id = db.Column(db.Integer, unique=True)
    item = db.Column(db.String(2000), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    requestor = db.Column(db.String(2000), nullable=False)
    price = db.Column(db.Numeric(20,2))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # approver_id= db.Column(db.Integer, db.ForeignKey('approver_id'))

    def __init__(self, name, morpheus_id, item, status, requestor, price):
        self.id
        self.name = name
        self.morpheus_id = morpheus_id
        self.item = item
        self.status = status
        self.requestor = requestor
        self.price = price
        self.timestamp
    
    def create_record(self):
        db.session.add(self)
        db.session.commit()

    def get_records():
        return RequestItems.query.all()

    def get_one(self):
        return RequestItems.query.get(self.id).all()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'morpheus_id': self.morpheus_id,
            'item': self.item,
            'requestor': self.requestor,
            'status': self.status,
            'price': str(self.price),
            'timestamp': self.timestamp
        }