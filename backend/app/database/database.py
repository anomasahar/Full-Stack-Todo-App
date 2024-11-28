from sqlmodel import create_engine, SQLModel
from app.configuration import setting

#Create Engine ~ one for whole application
connection_string: str = str(setting.DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, connect_args={"sslmode": "require"}, pool_recycle=300, pool_size=10, echo=True)

#Create Table
def create_tables():
    SQLModel.metadata.create_all(engine)