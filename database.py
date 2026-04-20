from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://meu_banco_8d57_user:WT5zgNizHvWpx7hPeCI0pYyeKQzxeayN@dpg-d7go5u7aqgkc739gqot0-a.oregon-postgres.render.com/meu_banco_8d57"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()