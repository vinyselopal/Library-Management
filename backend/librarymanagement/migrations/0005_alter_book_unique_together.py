# Generated by Django 4.2.7 on 2023-11-04 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarymanagement', '0004_book_average_rating_book_isbn_book_isbn13_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set(),
        ),
    ]
