from django.db import models

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    publisher = models.TextField(null=True)
    detail_url = models.TextField()
    book_image = models.TextField()
    published_date = models.DateField()
    content = models.TextField(null=True)

    def __str__(self):
        return self.title
