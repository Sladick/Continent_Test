# Generated by Django 3.2.8 on 2021-10-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_page', '0006_auto_20211007_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(default='http://127.0.0.1:8000/api/video/<built-in function id>/', max_length=255, unique=True, verbose_name='Url'),
        ),
    ]
