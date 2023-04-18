from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=60)
    body = models.CharField(max_length=100)
    create_at = models.DateField()
    author = models.CharField(max_length=30)


class Comment(models.Model):
    text = models.CharField(max_length=30)
    date = models.DateField()
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)


class Mark(models.Model):
    mark_value = models.CharField(max_length=20, choices=[
        ('Likes', 'Likes'),
        ('Dislike', 'Dislike')
    ])
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
