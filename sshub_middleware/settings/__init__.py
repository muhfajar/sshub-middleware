import random

from .base import *

try:
    from .private import *
except ImportError:
    raise ImportError("""
    Please create private.py file
    with contain configuration for 
    ====================================
    SECRET_KEY = '{}'
    DEBUG = False
    ALLOWED_HOSTS = []
    ====================================
    """.format(''.join([random.SystemRandom().
                       choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])))
