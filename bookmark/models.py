from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('사이트 주소')

    def __str__(self):
        return self.site_name + " : " + self.url