from .db_routing.routing_sqlalchemy import RoutingSQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db = RoutingSQLAlchemy()




class RoutingSqlAlchemy():

    def session(self):
        engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/data_master")
        Connection = sessionmaker(bind=engine)
        return Connection()