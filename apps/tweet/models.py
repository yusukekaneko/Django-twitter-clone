from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
   title = models.CharField(max_length=100)
   content = models.TextField()
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.title

   class Meta:
       ordering = ["-created_at"]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
