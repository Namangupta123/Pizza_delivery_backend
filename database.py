from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

postgresURL=os.getenv("POSTGRES_URL")
engine=create_engine(postgresURL,
    echo=True
)

Base=declarative_base()

Session=sessionmaker()