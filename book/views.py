from rest_framework import viewsets, permissions, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from book.models import Book, Member
from book.serializers import BookSerializer, MemberSerializer


# You can control which CRUD functions are allowed by adding the mixins to handle the functions you want to allow
class BookViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data['owner'] = Member.objects.get(id=request.data['owner']['id'])
                book = serializer.save()
                # book.save()
                return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            pass

        return Response(status=status.HTTP_400_BAD_REQUEST)


class MemberViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    #  can add methods for custom non-CRUD functionality
    @action(detail=False, methods=['GET'], url_path='like_book/(?P<member_id>\d+)/(?P<book_id>\d+)')
    def like_book(self, request, member_id, book_id):

        try:
            book = Book.objects.get(id=book_id)
            member = Member.objects.get(id=member_id)

            if book in member.books_liked.all():
                member.books_liked.remove(book)
            else:
                member.books_liked.add(book)

            return Response(BookSerializer(book).data, status=status.HTTP_200_OK)

        except Exception as ex:
            pass

        return Response(status=status.HTTP_400_BAD_REQUEST)
















    '''
    # we can override any of the CRUD functions
    def create(self, request, *args, **kwargs):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                book = serializer.save()
                book.title = f'saved_{book.title}'
                book.save()
                return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            pass

        return Response(status=status.HTTP_400_BAD_REQUEST)
    '''
