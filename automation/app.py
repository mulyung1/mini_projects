#app.py     https://www.kubeblogs.com/build-databases-with-sqlalchemy-and-alembic

from model import Base, engine
from icecream import ic


#initialise db(crate the db)
def init_db():
    Base.metadata.create_all(engine)
    ic('initialised db')

if __name__ == __main__:
    init_db()

