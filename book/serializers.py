from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'checked_out_to', 'liked_by')
        #  we can control what data is allowed to be sent out. This means we can restrict data based on roles.
