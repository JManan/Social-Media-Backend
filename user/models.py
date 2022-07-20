from django.db import models
from django.contrib.auth.models import User 
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    age = models.IntegerField(default=0)
    address = models.TextField(default="Blank")
    number = models.IntegerField(default=0)
    followers = models.ManyToManyField(User, blank=True, related_name="followers")
    email_receivers = models.ManyToManyField(User, blank=True, default=False, related_name="email_receivers")
    


    def __str__(self):
        return f'{self.user.username} Profile'

# profile_instance = Profile.objects.get(id = 3)
# print(profile_instance)
    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (3, 3)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)