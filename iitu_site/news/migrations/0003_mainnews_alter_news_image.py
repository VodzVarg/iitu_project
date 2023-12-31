# Generated by Django 4.2.2 on 2023-06-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_images/')),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Main news',
            },
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news_images/'),
        ),
    ]
