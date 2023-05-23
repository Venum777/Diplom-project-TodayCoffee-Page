from random import choices, randint
import string

print(''.join(choices(string.ascii_lowercase + str(randint(0, 9)), k=20)))