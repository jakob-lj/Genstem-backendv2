
from django.utils import timezone
import random

import datetime

def loginCode():
    return random.randint(1e5+1, 1e6-1)


