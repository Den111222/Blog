from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    category = models.ForeignKey('Category',
                                 verbose_name='Category',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Text')
    published_date = models.DateTimeField(verbose_name='published_date',)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    rate = models.IntegerField()
    def __str__(self):
        return f'{self.title}'

class Category(models.Model):
    text = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.text}'