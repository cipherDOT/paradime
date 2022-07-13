from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    # has a user as a foreignkey, so each Note has a user attribute, which is given
    # in views by
    # ```
    #   form.instance.user = request.user
    # ```
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.heading

class Answer(models.Model):
    # has a user as a foreignkey, so each Note has a user attribute, which is given
    # in views by
    # ```
    #   form.instance.user = request.user
    # ```
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.body

