from django.test import Client, TestCase
from librarymanagement.views import members_index


class UrlTests(TestCase):
    def test_members_index_post_url(self):
        response = self.client.post(
            "/librarymanagement/members",
            {"email": "a@gmail.com"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_members_index_get_url(self):
        response = self.client.get(
            "/librarymanagement/members",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_crud_members_get_url(self):
        response = self.client.get(
            "/librarymanagement/members/1",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_crud_members_put_url(self):
        response = self.client.put(
            "/librarymanagement/members/1",
            {"updated_fields": {"email": "b@gmail.com"}},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_crud_members_delete_url(self):
        response = self.client.delete(
            "/librarymanagement/members/1",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
