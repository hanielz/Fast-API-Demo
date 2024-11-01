from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:T1ku$H1t4m@localhost/sampledb"
#SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('postgres')}:{os.getenv('P@ssw0rd')}@localhost/sampledb"



engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
