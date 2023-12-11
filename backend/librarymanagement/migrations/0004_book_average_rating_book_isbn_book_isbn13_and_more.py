# Generated by Django 4.2.7 on 2023-11-04 12:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        (
            "librarymanagement",
            "0003_remove_member_name_book_authors_book_quantity_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="average_rating",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="isbn",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="isbn13",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="language_code",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="num_pages",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="publication_date",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="publisher",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="ratings_count",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="text_reviews_count",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="quantity",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="email",
            field=models.EmailField(max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="issue_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="return_date",
            field=models.DateField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name="book",
            unique_together={("title", "authors")},
        ),
    ]
