# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Forms(models.Model):
    ProfilePicture = models.CharField(max_length=1000)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=500)
    Mobile = models.CharField(max_length=12)
    National_ID = models.CharField(max_length=40)
    University = models.CharField(max_length=100)
    Faculty = models.CharField(max_length=100)
    Major = models.CharField(max_length=100)
    Minor = models.CharField(max_length=100)
    Expected_GraduationYear = models.CharField(max_length=4)