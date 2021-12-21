'''
imports base model from django
'''


from django.db import models


# Create your models here.
# Models are Tables added to your DB
'''
- Charfield must have characters or text in it
- max_length=50, stops names being longer than 50 characters.
- null=false prevents items being created without a name.
- blank=false stops form areas from being left blank.
- Boolean is true/false, on/off etc.
- default=False is to make sure TO DO Items are marked as not done by default.
'''
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    ''' resets the string to display name from db in admin
    instead of the ObjectId '''
    def __str__(self):
        return self.name
