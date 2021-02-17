"""Seed file to make sample data for db."""

from models import *
from app import app

# Create all tables
db.drop_all()
db.create_all()


c1 = Cupcake(flavor="chocolate", size='small', rating=2,
             image="http://s3.amazonaws.com/pix.iemoji.com/images/emoji/apple/ios-12/256/cupcake.png")
c2 = Cupcake(flavor="plain", size='large', rating=10,
             image="https://findicons.com/files/icons/792/cupcakes/256/cupcakes_christmas.png")
c3 = Cupcake(flavor="berry", size='medium', rating=6)

db.session.add_all([c1, c2, c3])
db.session.commit()
