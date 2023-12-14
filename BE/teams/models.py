from django.db import models

def team_thumbnail_path(instance, filename):
    return f'team_thumbnails/team_{instance.id}/{filename}'


class Team(models.Model):
    CATEGORY_CHOICES = [
        ('독서모임', '독서모임'),
        ('합평모임', '합평모임'),
        ('책집필모임', '책집필모임'),
    ]
    name = models.CharField(max_length=20, null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    is_closed = models.BooleanField(default=False)
    location = models.TextField(null=True, blank=True)
    max_attendance = models.IntegerField()
    current_attendance=models.IntegerField(default=0)
    introduce = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=team_thumbnail_path, null=True, blank=True)

    def __str__(self):
        return self.name