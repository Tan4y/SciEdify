from django.db import models
from django.urls import reverse

class Mathematics(models.Model):
    title = models.CharField(max_length=30, help_text='Topic title')
    text = models.CharField(max_length=6000, help_text='All information')

    class Meta:
        ordering = ['title']
        ordering = ['text']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.title

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.text

    