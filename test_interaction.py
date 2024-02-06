from contextlib import contextmanager

from Database_model import User, engine, Tracks_Sales
from sqlalchemy.orm import Session



with Session(bind=engine) as session:
    new_user = User(username='test', name='test',
                    email_address='test@test.com',
                    phone_number='test', gender='test')
    session.add(new_user)
    session.commit()

    new_user = session.query(User).filter_by(id).all()
    print(new_user)

# To be implemented for transaction scope
# @contextmanager
# def session_scope(engine):
#     """Provide a transactional scope around a series of operations."""
#     session = Session(engine)
#     try:
#         yield session
#         session.commit()
#     except:
#         session.rollback()
#         raise