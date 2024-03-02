from Database_model import User, Session, create_engine, Trucks
from create_fields.new_user import NewUser
from create_fields.create_vehicle_ad import TruckAd
from sqlalchemy import text
from datetime import datetime
from config import settings
from conn_to_database import connect_to_postgresql
from API.Validators.user_input.gender_valid import gender_validator_func
from API.Validators.user_input.phone_number_valid import phone_number_validator_func
from API.Validators.user_input.email_valid import email_validator_func
from API.Validators.user_input.name_valid import name_validator_func
from API.Validators.user_input.username_valid import username_validate_func


def create_new_user() -> None:
    while True:
        connect = input("Please choose option:\n1. [Connecting using environment variables]"
                        " \n2. [Connecting using user input] "
                        "\n3. [Exit]\n: ")
        if connect == '1' or connect.lower() == 'connecting using environment variables':
            engine = create_engine(settings.DATABASE_URL_psycopg)
            break
        elif connect == '2' or connect.lower() == 'connecting using user input':
            engine = create_engine(connect_to_postgresql())
            break
        elif connect == '3' or connect.lower() == 'exit':
            raise Exception('Exit')
        else:
            print("Invalid option")

    with Session(bind=engine) as session:
        try:
            session.execute(text('SELECT 1'))
            print('\n\033[1;32;40mDatabase is connected\033[0m')
        except:
            raise Exception('\n\033[1;31;40mCannot connect to database\033[0m')
        print("\nPlease fill in the following fields: ")
        username = username_validate_func(input('Username: '), echo=True)
        name = name_validator_func(input('Name: '), echo=True)
        email_address = email_validator_func(input('Email address: '), echo=True)
        phone_number = phone_number_validator_func(input('Phone number: '), echo=True)
        gender = gender_validator_func(input('Gender: '), echo=True)
        create_user = NewUser.model_validate({
            'username': username,
            'name': name,
            'email_address': email_address,
            'phone_number': phone_number,
            'gender': gender})
        new_user = User(**create_user.key_args())
        session.add(new_user)

        try:
            print('Saving new user...Please wait...')
            session.commit()
            print('\n\033[1;32;40mSuccess. Your account has been created\033[0m')
        except Exception as e:
            session.rollback()
            print('\n\033[1;31;40mFailed. Your account has not been created\033[0m')
            print(e)

# def create_truck(engine):
#     with Session(bind=engine) as session:
#         try:
#             session.execute(text('SELECT 1'))
#             print('Database is connected')
#         except:
#             raise Exception('Database is not connected')
#
#         t = TruckAd(user_id=1, maker="test", model="test", price=1000,
#                     condition="test", fuel="test", power_output=100,
#                     gearbox="test", mileage=100, used=True,
#                     color="black", primary_registration=datetime.now(),
#                     manufactured_date=datetime.now(),
#                     engine_volume=1.6, average_consumption=5.5,
#                     vin_number="12345678test")
#
#         new_truck = Trucks(**t.key_args())
#         session.add(new_truck)
#
#         try:
#             print('Transaction started')
#             session.commit()
#             print('Transaction committed')
#         except:
#             session.rollback()
#             print('Transaction failed')


create_new_user()