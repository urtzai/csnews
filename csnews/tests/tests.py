from django.test import TestCase
from datetime import datetime
try:
    from django.core.urlresolvers import reverse
except ImportError:  # django < 1.10
    from django.urls import reverse
from django.test import Client
from csnews.models import Article
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:  # django < 1.5
    from django.contrib.auth.models import User


class BasicTest(TestCase):
    def setUp(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Article.objects.create(title="First new", slug="first-new", summary="This is the summary.", body="This is the first new.", published=datetime.now())

    def test_csnews_index_view(self):
        c = Client()
        url = reverse('csnews_index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_index_view(self):
        c = Client()
        url = reverse('csnews_display', kwargs={'article_slug': "first-new"})
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_archive_view(self):
        c = Client()
        url = reverse('csnews_archive')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_feed_view(self):
        c = Client()
        url = reverse('csnews_feed')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)
