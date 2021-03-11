from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='media/director_images/')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

def generatePath(self, filename):
    url='media/films/%s/%s'% (self.folder, filename)
    return url

class Film(models.Model):
    title = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.PROTECT)
    date = models.DateField(null=False, blank=False)
    date_upload = models.DateField(auto_now_add=True)
    synopsis = models.TextField(null=False, blank=False)
    folder = models.CharField(max_length=20)
    video = models.FileField(upload_to=generatePath)
    subtitle = models.FileField(upload_to=generatePath, null=True, blank=True)
    img = models.ImageField(upload_to=generatePath, null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
