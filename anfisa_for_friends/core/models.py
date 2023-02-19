from django.db import models

class PublishedModel(models.Model):
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    title = models.CharField(max_length=256, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
