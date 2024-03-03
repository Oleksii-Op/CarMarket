from database_model import User, create_engine, Address
from create_fields.new_user import NewUser
from create_fields.create_address import UserAddress
from sqlalchemy import text, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from config import settings
from conn_to_database import connect_to_postgresql
from API.Validators.user_input.gender_valid import gender_validator_func
from API.Validators.user_input.phone_number_valid import phone_number_validator_func
from API.Validators.user_input.email_valid import email_validator_func
from API.Validators.user_input.name_valid import name_validator_func
from API.Validators.user_input.username_valid import username_validate_func
from API.Validators.address_input.address_valid import address_validator_func
from API.Validators.address_input.state_valid import state_validator_func
from API.Validators.address_input.zip_code_valid import zip_code_validator_func
import hashlib


def create_new_user() -> None:
    """
    Function to create a new user with user input,
    including database connection, user data validation,
    hashing and saving user information to the database.
    """

    while True:
        connect = input("Please choose option:\n1. [Connecting using environment variables]"
                        " \n2. [Connecting using user input] "
                        "\n3. [Exit]\n: ")
        if connect == '1' or connect.lower() == 'connecting using environment variables':
            engine = create_engine(settings.DATABASE_URL_psycopg, echo=True)
            break
        if connect == '2' or connect.lower() == 'connecting using user input':
            engine = create_engine(connect_to_postgresql(), echo=True)
            break
        if connect == '3' or connect.lower() == 'exit':
            return
        else:
            print("Invalid option")

    with Session(bind=engine) as session:
        try:
            session.execute(text('SELECT 1'))
            print('\n\033[1;32;40mDatabase is connected\033[0m')
        except:
            raise Exception('\n\033[1;31;40mCannot connect to database\033[0m')

        print("\nPlease fill in the following fields: ")

        username = username_validate_func(input('(Compulsory field) Username: '), echo=True)
        fist_name = name_validator_func(input('(Compulsory field) First name: '), echo=True)
        last_name = name_validator_func(input('(Compulsory field) Last name: '), echo=True)
        email_address = email_validator_func(input('(Compulsory field) Email address: '), echo=True)
        phone_number = phone_number_validator_func(input('(Compulsory field) Phone number: '), echo=True)
        gender = gender_validator_func(input('Gender [male, female, other, unknown]: '), echo=True)

        country = input('(Compulsory field) Country : ')
        city = input('(Compulsory field) City: ')
        state = state_validator_func(input('State: '), echo=True)
        zip_code = zip_code_validator_func(input('(Compulsory field) Zip code: '), echo=True)
        street_address = address_validator_func(input('Street address: '), echo=True)
        address_hashable = hashlib.sha256(
            (country + city + street_address).encode('utf-8')).hexdigest()

        create_address = UserAddress.model_validate({
            'country': country,
            'city': city,
            'state': state,
            'zip_code': zip_code,
            'address': street_address,
            'address_hash': address_hashable
        })

        transaction_address = Address(**create_address.key_args())
        try:
            session.add(transaction_address)
            session.commit()
            stmt = select(Address.address_id).where(Address.address_hash == address_hashable)
            address_id = session.execute(stmt).scalar()

            create_user = NewUser.model_validate({
                'username': username,
                'first_name': fist_name,
                'last_name': last_name,
                'email_address': email_address,
                'main_phone_number': phone_number,
                'additional_phone_number': None,
                'gender': gender,
                'address_id': address_id})

            transaction_user = User(**create_user.key_args())
            session.add(transaction_user)

            print('Saving new user...Please wait...')
            session.commit()
            print('\n\033[1;32;40mAddress saved.\033[0m')
            print('\n\033[1;32;40mSuccess. Your account has been created\033[0m')

        except IntegrityError as e:
            session.rollback()
            print('\n\033[1;31;40mFailed. Your account has not been created\033[0m')
            print(e)
            print('Rolled back')

create_new_user()
