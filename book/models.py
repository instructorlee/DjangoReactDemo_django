from django.db import models


# an ABSTRACT model will attach all its attributes and functions to any model that inherits it.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Member(BaseModel):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(BaseModel):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.FloatField(default=0)

    owner = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='books')
    checked_out_to = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, default=None, blank=True,
                                       related_name='checkedout_books')
    liked_by = models.ManyToManyField(Member, related_name='books_liked', blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
