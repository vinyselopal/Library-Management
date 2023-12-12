from django.test import TestCase
from librarymanagement.models import Book, Transaction, Member
from librarymanagement.views import issue_book
from datetime import datetime, timedelta


class ViewsTest(TestCase):
    def setUpTestData(cls):
        members = [{"email": "a@gmail.com"}, {"email": "b@gmail.com"}]
        transactions = [
            {
                "book_id": "1",
                "member_id": "1",
                "issue_date": datetime.now() - timedelta(days=10),
                "return_date": datetime.now() - timedelta(days=3),
                "payment_done": False,
            }
        ]
        books = [{"book_title": "1984", "book_author": "George Orwell"}]
        Member.objects.bulk_create(members)
        Transaction.objects.bulk_create(transactions)
        Book.objects.bulk_create(books)

    def testIssueBookView(self):
        response = self.client.post(
            "/members/issue_book",
            {
                "book_title": "1984",
                "issue_date": datetime.now(),
                "member_email": "a@gmail.com",
            },
        )
        self.assertEqual(response.status_code, 200)
