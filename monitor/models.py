from __future__ import unicode_literals

from django.db import models


class UserLog(models.Model):
    session_id = models.CharField(max_length=20)
    login_date = models.DateTimeField('login date')