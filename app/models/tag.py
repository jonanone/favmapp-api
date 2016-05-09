from app import db
from app.error_handler import InvalidUsage
from datetime import datetime


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.now())
    editedAt = db.Column(db.DateTime, default=datetime.now())
    deletedAt = db.Column(db.DateTime, nullable=True)

    @property
    def serialize(self):
        # Returns object data in easily serializable format
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'createdAt': self.createdAt,
            'editedAt': self.editedAt,
            'deletedAt': self.deletedAt
        }

    @classmethod
    def create(cls, name, description=None):
        if name is None or name == '':
            raise InvalidUsage('Bad Request', status_code=400)
        else:
            tag = Tag(name=name,
                      description=description)
            db.session.add(tag)
            db.session.commit()
            return tag


    def update(self, name=None, description=None):
        # using "if A is not None and A != ''" because is faster than just
        # using "if A", since "if A" will call A.__nonzero__() function
        # which checks more stuff.
        if name is not None and name != '':
            self.name = name

        if description is not None:
            self.description = description

        self.editedAt = datetime.now()
        db.session.add(self)
        db.session.commit()
        return self


    def delete(self):
        self.editedAt = datetime.now()
        self.deletedAt = datetime.now()
        db.session.add(self)
        db.session.commit()
        return 1


    @classmethod
    def get_all(cls):
        query = db.session.query(Tag).filter(Tag.deletedAt == None)
        return query


    @classmethod
    def get(cls, tag_id):
        query = db.session.query(Tag).filter(Tag.id == tag_id).first()
        return query


    @classmethod
    def get_deleted(cls):
        query = db.session.query(Tag).filter(Tag.deletedAt != None)
        return query
