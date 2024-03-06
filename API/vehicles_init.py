from database_model import Vehicle, create_engine
from sqlalchemy.orm import Session
import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from API.config import settings


def insert_vehicle_from_csv(csv: str):
    # TODO: Doc string
    frame = pd.read_csv(csv, usecols=['brand', 'model', 'category_id'])

    engine = create_engine(settings.DATABASE_URL_psycopg, echo=True)

    with Session(bind=engine) as session:
        # Raises exception if no connection established
        session.execute(text('SELECT 1'))
        print('\n\033[1;32;40mDatabase is connected\033[0m')

        # All or nothing transaction
        session.begin(nested=True)
        try:
            for _, row in frame.iterrows():
                brand = row['brand']
                model = row['model']
                category = row['category_id']

                vehicle = Vehicle(make=brand, model=model, category=category)
                session.add(vehicle)
                session.commit()
        except (IntegrityError, InvalidRequestError) as error:
            print('Something went. Check your database or data.')
            session.rollback()
            print('Session rolled back')
            raise Exception(error)
