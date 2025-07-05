from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://Cibertec_owner:npg_vDk94IenXajr@ep-plain-forest-a4m3tip4-pooler.us-east-1.aws.neon.tech/Cibertec?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
