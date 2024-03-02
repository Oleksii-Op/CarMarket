import random
from string import ascii_letters, digits
from faker import Faker


class RandomUser:
    country_codes = ['+380', '+372', '+371', '+370']
    country_phones = {
        'ukraine': {'Vodafone Mobile': ['050', '066', '095', '099'],
                    'Kyivstar': ['067', '068', '096', '097', '098'],
                    'Lifecell': ['063', '073', '093']},
        'estonia': {'common': ['5x', '81', '82', '83', '84']},
        'latvia': {'common': '2'},
        'lithuania': {'common': '6'}
    }
    fake = Faker()

    def __init__(self) -> None:
        self.name = self.random_name()
        self.email = self.random_email()
        self.phone = self.random_phone()
        self.gender = self.random_gender()
        self.username = self.random_username()

    @staticmethod
    def random_name() -> str:
        names_gen = [RandomUser.fake.name().split()[0] for _ in range(100)]
        return random.choice(names_gen)

    @staticmethod
    def random_gender() -> str:
        return random.choice(['male', 'female', 'other', 'unknown'])

    @staticmethod
    def random_phone() -> str:
        country_code = random.choice(RandomUser.country_codes)
        if country_code == '+380':
            carrier = random.choice(list(RandomUser.country_phones['ukraine'].keys()))
            carrier_prefix = random.choice(RandomUser.country_phones['ukraine'][carrier])
            phone_number = str(random.randint(1000000, 9999999))
            return f'{country_code}{carrier_prefix}{phone_number}'
        elif country_code == '+372':
            carrier = random.choice(RandomUser.country_phones['estonia']['common'])
            if carrier == '5x':
                carrier = '5' + str(random.randint(0, 9))
        elif country_code == '+371':
            carrier = RandomUser.country_phones['latvia']['common'] + str(random.randint(0, 9))
        elif country_code == '+370':
            carrier = RandomUser.country_phones['lithuania']['common'] + str(random.randint(0, 9))
        phone_number = str(random.randint(100000, 999999))
        return f'{country_code}{carrier}{phone_number}'

    @staticmethod
    def random_email() -> str:
        name = ''.join(random.choice(
            ascii_letters + digits) for _ in range(10))
        domain = random.choice(['gmail.com', 'yahoo.com'])
        return f'{name}@{domain}'

    def random_username(self) -> str:
        name = self.name
        add_len = random.randint(1, 19 - len(name))
        username = ''.join(random.choice(
            ascii_letters + digits) for _ in range(add_len))
        return name + username

    def generate_user(self) -> dict:
        return {
            'username': self.username,
            'name': self.name,
            'email_address': self.email,
            'phone_number': self.phone,
            'gender': self.gender
        }

    def __repr__(self):
        return (f"RandomUser(username={self.username},"
                f" name={self.name}, email={self.email},"
                f" phone={self.phone}, gender={self.gender})")

