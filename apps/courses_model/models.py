from __future__ import unicode_literals
from django.db import models
from ..login_reg_app.models import User

class Course(models.Model):
      name = models.CharField(max_length=255)
      description = models.TextField(max_length=1000)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      person = models.ForeignKey(User)
