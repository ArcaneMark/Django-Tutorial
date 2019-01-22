
"""
This will create a model.
"""
from django.db import models

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)



"""
This will create an Admin Interface
"""
from django.contrib import admin

from . import models

admin.site.register(models.Article)
