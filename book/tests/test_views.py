from django.test import TestCase


class BookIndexViewTestCase(TestCase):

    def test_can_render(self):
        res = self.client.get('/books/')
        self.assertContains(res, 'hello')
