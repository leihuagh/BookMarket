from django.test import TestCase
from reference.models import Author
from django.test import Client
# Create your tests here.


class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(name="Пушкин", description="Про Пушкина")
        Author.objects.create(name="Лермонтов", description="Про Лермонтова")

    def test_long_author_str(self):
        long_author = 'Пушкин'*100
        my_author = Author.objects.create(name="Пушкин", description="Про Пушкина")
        obj = Author.objects.create(name=long_author, description='about')
        self.assertEqual(str(obj.name), my_author)


    def test_author_str(self):
        """Animals that can speak are correctly identified"""
        pushkin = Author.objects.get(name="Пушкин")
        lermontov = Author.objects.get(name="Лермонтов")
        self.assertEqual(str(pushkin), 'Пушкин')
        self.assertEqual(str(lermontov), 'Лермонтов')


class ClientTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_template_reference_list(self):
        response = self.c.get('/reference/author-ref-list/')
        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'reference/ref-list-base.html')

    def test_template_reference_create_update(self):
        response = self.c.post('/accounts/login/', {'username': 'anton', 'password': '123321'})
        self.assertEquals(response.status_code, 200)