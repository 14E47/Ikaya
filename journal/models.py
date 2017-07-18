from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

class Journal(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()    
    slug = models.SlugField(max_length=100, unique=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = "Journal"
        verbose_name_plural = "Journals"

    def get_absolute_url(self):
        return self.slug

    def images(self):
        images = JournalImage.objects.filter(journal=self)
        return images

    def youtube_urls(self):
        urls = JournalYoutube.objects.filter(journal=self)
        return urls

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Journal, self).save(*args, **kwargs)

class JournalImage(models.Model):
    image = models.ImageField(blank=True, upload_to='uploads/images')
    journal = models.ForeignKey(Journal)

    class Meta:
        verbose_name = "Journal Image"
        verbose_name_plural = "Journal Images"

class JournalYoutube(models.Model):
    url = models.CharField(max_length=250)
    journal = models.ForeignKey(Journal)

    class Meta:
        verbose_name = "Journal Youtube Url"
        verbose_name_plural = "Journal Youtube Urls"        