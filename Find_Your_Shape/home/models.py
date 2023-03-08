from django.db import models

# Create your models here.


class hiitbook(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    focus = models.CharField(max_length=50, null=False, blank=False)
    time = models.DateTimeField(max_length=10)

    def __str__(self):
        return self.name


class SpinClasses(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    genre = models.CharField(max_length=10, null=False, blank=False)
    time = models.DateTimeField(max_length=10)

    def __str__(self):
        return self.name


class hittclasses(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    trainer = models.CharField(max_length=10, null=False, blank=False)
    focus = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class PtClasses(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    trainer = models.CharField(max_length=10, null=False, blank=False)
    focus = models.CharField(max_length=50, null=False, blank=False)
    time = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.name
