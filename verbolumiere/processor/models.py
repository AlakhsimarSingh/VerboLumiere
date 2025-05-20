from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UploadedVideo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    original_video = models.FileField(upload_to="original/")
    transcript = models.TextField(blank=True, null=True)
    translated_audio = models.FileField(upload_to="translated/audio/",blank=True,null=True)
    translated_video = models.FileField(upload_to="translated/video/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s video {self.id}"