from API.Validators.user_input.email_valid import email_validator_func_perf
from API.Validators.user_input.phone_number_valid import phone_number_validator_func_perf
from API.Validators.user_input.username_valid import username_validate_func_perf
from API.Validators.user_input.name_valid import name_validator_func_perf
from API.Validators.user_input.gender_valid import gender_validator_func_perf

import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import pandas as pd
from faker import Faker
fake = Faker('en_GB')  # Great Britain region related fake data.


class UserValidationPerformance:
    # TODO: Refactoring
    validators = {
        'email': email_validator_func_perf,
        'username': username_validate_func_perf,
        'main_phone_number': phone_number_validator_func_perf,
        'first_last_name': name_validator_func_perf,
        'gender': gender_validator_func_perf
    }

    fake = Faker('en_GB')
    def __init__(self, csv_file_path=None):
        if csv_file_path:
            self.csv_file = csv_file_path
            self.df = pd.read_csv(
                self.csv_file, usecols=['username', 'first_name', 'last_name',
                            'email_address', 'main_phone_number', 'gender'])

            self.result, self.number_of_iterations = self.test()
        else:
            default = 1000
            print(f'CSV file not found. Generating {default} users to be tested by default')
            self.df = self.generate_data(default)
            self.result, self.number_of_iterations = self.test()

    def test(self):
        counter_dict = Counter()
        count = 0
        for _, row in self.df.iterrows():
            if self.validators['email'](row['email_address']):
                counter_dict.update({'email_valid': 1})
            else:
                counter_dict.update({'email_invalid': 1})

            if self.validators['main_phone_number'](row['main_phone_number']):
                counter_dict.update({'phone_number_valid': 1})
            else:
                counter_dict.update({'phone_number_invalid': 1})

            if self.validators['username'](row['username']):
                counter_dict.update({'username_valid': 1})
            else:
                counter_dict.update({'username_invalid': 1})

            if self.validators['first_last_name'](row['first_name']):
                counter_dict.update({'first_name_valid': 1})
            else:
                counter_dict.update({'first_name_invalid': 1})

            if self.validators['first_last_name'](row['last_name']):
                counter_dict.update({'last_name_valid': 1})
            else:
                counter_dict.update({'last_name_invalid': 1})

            if self.validators['gender'](row['gender']):
                counter_dict.update({'gender_valid': 1})
            else:
                counter_dict.update({'gender_invalid': 1})
            count += 1

        return counter_dict, count

    def generate_data(self, number):
        field_names = ['username', 'first_name', 'last_name', 'email_address',
                       'main_phone_number','gender']

        user_df = pd.DataFrame(columns=field_names)

        user_df['username'] = [fake.user_name() for _ in range(number)]
        user_df['first_name'] = [fake.first_name() for _ in range(number)]
        user_df['last_name'] = [fake.last_name() for _ in range(number)]
        user_df['email_address'] = [fake.email() for _ in range(number)]
        user_df['main_phone_number'] = [fake.phone_number() for _ in range(number)]
        user_df['gender'] = [random.choice(
            ['male', 'female', 'other', 'unknown']) for _ in range(number)]

        return user_df

    def visual_results(self):
        scores_by_test = {
            'Email validation success': self.result['email_valid'],
            'Email validation failed': self.result['email_invalid'],
            'Phone number validation success': self.result['phone_number_valid'],
            'Phone number validation failed': self.result['phone_number_invalid'],
            'Username validation success': self.result['username_valid'],
            'Username validation failed': self.result['username_invalid'],
            'First Name validation success': self.result['first_name_valid'],
            'First Name validation failed': self.result['first_name_invalid'],
            'Last Name validation success': self.result['last_name_valid'],
            'Last Name validation failed': self.result['last_name_invalid'],
            'Gender validation success': self.result['gender_valid'],
            'Gender validation failed': self.result['gender_invalid']
            }



        colors = ['green' if 'success' in test else 'red' for test in scores_by_test.keys()]

        fig, ax1 = plt.subplots(figsize=(9, 7), layout='constrained')
        fig.canvas.manager.set_window_title('User data validation results')

        ax1.set_title('Data validators performance')
        ax1.set_xlabel(
            'Number of users iterated over')

        validators = list(scores_by_test.keys())
        values = list(scores_by_test.values())

        rects = ax1.barh(validators, values, align='center', height=0.5, color=colors)


        log_step = np.ceil(np.log10(self.number_of_iterations)) - 1
        x_ticks_step = int(10 ** log_step)

        ax1.set_xlim([0, self.number_of_iterations])
        ax1.set_xticks(np.arange(0, self.number_of_iterations + x_ticks_step, x_ticks_step))
        ax1.xaxis.grid(True, linestyle='--', which='major',
                       color='grey', alpha=.25)
        ax1.axvline(50, color='grey', alpha=0.25)  # median position

        ax2 = ax1.twinx()
        ax2.set_ylim(ax1.get_ylim())
        ax2.set_yticks(
            np.arange(len(scores_by_test)),
            labels=[score for score in scores_by_test.values()])

        ax2.set_ylabel('Test Scores')

        plt.show()


new = UserValidationPerformance()
new.visual_results()