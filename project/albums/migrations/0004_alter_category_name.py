# Generated by Django 5.1.1 on 2024-10-05 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_category_tag_article_delete_albums_delete_musician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
