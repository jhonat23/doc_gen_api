# Enviroment variables
from dotenv import load_dotenv
import os

# SQLAlchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Parsing .env file
load_dotenv()

# Getting database info
db_vars = [
    'MYSQLUSER',
    'MYSQLPASSWORD',
    'MYSQLHOST',
    'MYSQLPORT',
    'MYSQLDATABASE'
]

db_connect_data = {
    db_vars[i]: os.getenv(db_vars[i]) 
    for i in range(len(db_vars))
}

# Creating Engine a Session
## the dialect/DBAPI used is PyMySQL
engine = create_engine(
    f'mysql+pymysql://{db_connect_data[db_vars[0]]}:{db_connect_data[db_vars[1]]}@{db_connect_data[db_vars[2]]}:{db_connect_data[db_vars[3]]}/{db_connect_data[db_vars[4]]}'
)

# Creating a Session instance
LocalSession = sessionmaker(
    bind=engine,
    autocommit=False, 
    autoflush=False,
)

# Creating base for models
class Base(DeclarativeBase):
    pass