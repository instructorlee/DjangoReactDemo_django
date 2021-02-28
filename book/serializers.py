from rest_framework import serializers

from .models import Book, Member


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('id', 'first_name', 'last_name')


class BookSerializer(serializers.ModelSerializer):
    owner = MemberSerializer(read_only=True)
    checked_out_to = MemberSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'checked_out_to', 'liked_by', 'owner')
        #  we can control what data is allowed to be sent out. This means we can restrict data based on roles.
