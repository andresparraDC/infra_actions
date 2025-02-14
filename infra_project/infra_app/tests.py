from http import HTTPStatus

from django.test import Client, TestCase


class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности страниц."""
        urls_status = {
            '/': HTTPStatus.OK.value,
            '/second/': HTTPStatus.OK.value,
        }
        for urls, status in urls_status.items():
            with self.subTest(urls=urls):
                response = self.client.get(urls)
                self.assertEqual(response.status_code, status)

    def test_page_shows_correct_content(self):
        """Проверка контента страниц."""
        response = self.client.get('/')
        self.assertContains(response, 'У меня получилось!')

        response = self.client.get('/second/')
        self.assertContains(response, 'А это вторая страница')
