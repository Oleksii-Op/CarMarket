from collections import Counter
from UserGenerator.user_generator import RandomUser
from Generators.validators import (validate_name,
                                   validate_username, validate_email_address,
                                   validate_phone_number, validate)

import matplotlib.pyplot as plt
import numpy as np

counter = Counter()
n = 100
for _ in range(n):
    rand_user = RandomUser()

    counter['valid_name'] += int(validate_name(rand_user.name))
    counter['valid_username'] += int(validate_username(rand_user.username))
    counter['valid_email'] += int(validate_email_address(rand_user.email))
    counter['valid_phone'] += int(validate_phone_number(rand_user.phone))
    counter['valid_gender'] += int(validate(rand_user.gender))

counter['not_valid_name'] = n - counter['valid_name']
counter['not_valid_username'] = n - counter['valid_username']
counter['not_valid_email'] = n - counter['valid_email']
counter['not_valid_phone'] = n - counter['valid_phone']
counter['not_valid_gender'] = n - counter['valid_gender']

species = list(counter.keys())

x = np.arange(len(species))  # the label locations
width = 0.10  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in counter.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of users generated')
ax.set_title('Number of users generated per attribute')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, n + 10)

plt.show()
