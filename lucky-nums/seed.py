from app import app
from models import db, User

db.drop_all()
db.create_all()

u1 = User(
    name="Nick",
    email="sdfsdfs",
    year=1992,
    color="blue",
    lucky_num=23
)
