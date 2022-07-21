from django.db import models
from django.utils.timezone import activate
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class PostList(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_pb = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['-date_pb']

    def __str__(self):
        return f'{self.title} {self.description[0:3]}'

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.id})
    

class Comment(models.Model):
    post = models.ForeignKey(PostList, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    name = models.CharField(max_length=75)
    email = models.EmailField()
    date_pb = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_pb']

    def __str__(self):
        return f'{self.post} => {self.content[0:4]}'

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.post.id})