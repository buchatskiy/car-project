from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Model(models.Model):
    brands = models.ForeignKey(Brand)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
