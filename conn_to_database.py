from typing import Union


def select_database() -> Union[str, None]:
    """
       This function prompts the user to enter the name of
       the database they want to use. It validates the input
       and either returns the connection string for SQLite or
       calls the function to connect to PostgreSQL.
       Returns a string representing the database connection.
       """
    database = input("Please enter the name of the "
                     "database you want to use(SQLite or PostgreSQL: ").lower()

    answers = ['sqlite', 'postgresql']

    if database not in answers:
        msg = """Wrong input. Please choose one of the following databases:
        SQLite or PostgreSQL.
        If you use another database, please refer to your database documentation.
                """
        print(msg)
        raise ValueError(msg)

    if database == 'sqlite':
        return 'sqlite:///database.db'
    if database == 'postgresql':
        return connect_to_postgresql()


def create_connection_string(username: str,
                             password: str,
                             hostname: str,
                             port: str,
                             database_name: str) -> str:
    """
       Create a connection string for a PostgreSQL database.
       Args:
           username (str): The username for the database connection.
           password (str): The password for the database connection.
           hostname (str): The hostname for the database connection.
           port (str): The port for the database connection.
           database_name (str): The name of the database.
       Returns:
           str: The connection string for the PostgreSQL database.
       """
    return f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database_name}'


def connect_to_postgresql() -> str:
    """
        Connects to the PostgreSQL database using user input for username,
        password, hostname, port, and database name.
            str: Input string as a sqlalchemy.create_engine
             argument for PostgreSQL database.
        """

    print('Please enter the following details to create the connection string:')

    username = input('Username: ')
    password = input('Password: ')
    hostname = input('Hostname (default: localhost): ')
    port = input('Port (default: 5432): ')
    database_name = input('Database Name: ')

    if not hostname:
        hostname = 'localhost'
    if not port:
        port = '5432'

    connection_string = create_connection_string(username,
                                                 password, hostname, port, database_name)

    return connection_string

# engine = create_engine('sqlite:///database.db', echo=True)
