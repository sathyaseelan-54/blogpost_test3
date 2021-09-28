from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField()
    liked = models.ManyToManyField(User,default = None,blank = True,related_name = 'liked')
    body = models.TextField()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('detail',args = (str(self.id)))

    @property
    def num_likes(self):
        return self.liked.all().count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = "comments",on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    value = models.CharField(choices = LIKE_CHOICES,default = 'Like',max_length = 15)

    def __str__(self):
        return str(self.post)


