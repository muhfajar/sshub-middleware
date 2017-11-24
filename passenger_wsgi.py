#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  muhfajar - passenger_wsgi.py
#
#  Created by PyCharm.
#  User: fajar
#  Date: 5/16/17
#  Time: 8:21 PM
#
#

import sshub_middleware.wsgi

# load Django
application = sshub_middleware.wsgi.application
