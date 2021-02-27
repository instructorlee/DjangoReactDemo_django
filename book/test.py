from rest_framework.test import APITestCase

from .models import Book, Member

class TestBookViewSet(APITestCase):

    def test_custom_create(self):
        response = self.client.post('/book/', {
            'title': 'test_title',
            'author': 'test_author'
        })

        self.assertEqual(response.status_code, 201)

        self.assertEqual(response.data['title'], 'saved_test_title')


class TestMemberViewsSet(APITestCase):

    # for each test, the dB is cleared and the data in this method is added
    def setUp(self):
        self.book = Book.objects.create(title='test_book_title', author='test_book_title')
        self.member = Member.objects.create(first_name='Fred', last_name='Flintstone')

    def test_like_book(self):
        response = self.client.get(f'/member/like_book/{self.member.id}/{self.book.id}/')

        self.assertEqual(response.status_code, 200)

        member = Member.objects.get(id=self.member.id)
        self.assertTrue(self.book in member.books_liked.all())
