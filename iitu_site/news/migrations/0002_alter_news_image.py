# Generated by Django 4.2.2 on 2023-06-09 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news/news_images/'),
        ),
    ]
