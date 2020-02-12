import time
import datetime
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine


from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from model import Customer, Condition


Base = declarative_base()
DBSession = scoped_session(sessionmaker())
engine = None

class Utils:

    @staticmethod
    def create_connection(db_details):
        url = URL(**db_details)
        return url
    

    @staticmethod
    def create_URL(db_details):
        url = URL(**db_details)
        try:
            engine = create_engine(url)
            connection = engine.connect()
            # result = connection.execute("select * from payment_types")
            # for row in result:
            #     print(row)
            return connection
        except Exception as e:
            raise e


    @staticmethod
    def close_connection(connection):
        try:
            connection.close()
        except Exception as e:
            raise e


    @staticmethod
    def init_sqlalchemy(dbname='sqlite:///sqlalchemy.db'):
       
        global engine
        engine = create_engine(dbname, echo=False)
        DBSession.remove()
        DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)


    @staticmethod
    def test_sqlalchemy_core(db_url,n=10):
        """
            inserts 10000 records 1.1002159118652344 secs
        """
        try:
            Utils.init_sqlalchemy(dbname=db_url)
            t0 = time.time()
            engine.execute(
                Condition.__table__.insert(),
                [{"time":str(datetime.datetime.now()),"location": 'loc-{}'.format(i),"temperature":i} for i in range(n)]
            )
            print("SQLAlchemy Core: Total time for " + str(n) +" records "+str(time.time() - t0)+" secs")
        except Exception as e:
            print(e)
        
        