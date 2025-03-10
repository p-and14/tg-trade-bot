from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import config

from models import Base


engine = create_engine(f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}", echo=False)
session = Session(engine)

# Create tables
Base.metadata.create_all(engine)
