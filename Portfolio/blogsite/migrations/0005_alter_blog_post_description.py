# Generated by Django 4.1.3 on 2022-11-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0004_blog_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='description',
            field=models.TextField(),
        ),
    ]