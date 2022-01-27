from django.db import models
from django.db.models.deletion import CASCADE
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.conf import settings
User = settings.AUTH_USER_MODEL
#define job model and fields
class Job(models.Model):
    title = models.CharField(max_length=200, help_text="Job Title")
    description = models.TextField(help_text="Job Description")
    company = models.CharField(max_length=200, help_text="Company Name")
    location = models.CharField(max_length=200, help_text="Location")
    link = models.URLField(help_text="Link to Job")
    date = models.DateField(help_text="Publish Date")
    salary=models.IntegerField(('Salary'),null=True,blank=True)
    #users list applied to jobs
    users_applied = models.ManyToManyField(User, related_name='jobs_applied', blank=True)
    image = VersatileImageField(upload_to='images/', blank=True, null=True, ppoi_field='ppoi')
    ppoi = PPOIField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Jobs"


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name
