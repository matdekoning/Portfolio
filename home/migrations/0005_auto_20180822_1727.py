# Generated by Django 2.0.6 on 2018-08-22 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_article_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='full_name',
            new_name='url',
        ),
    ]
