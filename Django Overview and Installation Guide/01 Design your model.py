"""
Although you can use Django without a database, it comes with an object-relational mapper in which you describe your database layout in Python code.

The data-model syntax offers many rich ways of representing your models – so far, it’s been solving many years’ worth of database-schema problems. Here’s a quick example:
"""

from django.db import models

class Reporter(models.Model): #model correspond to a table
    full_name = models.CharField(max_length=70) #this reger to a field in a table

    def __str__(self):
        return self.full_name

class Article(models.Model): #model correspond to a table
    pub_date = models.DateField() #this reger to a field in a table
    headline = models.CharField(max_length=200) #this reger to a field in a table
    content = models.TextField() #this reger to a field in a table
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE) #this reger to a field in a table

    def __str__(self):
        return self.headline


#then run
#$ python manage.py migrate
