# Generated by Django 2.0.6 on 2018-08-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180822_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='full_name',
            field=models.CharField(blank=True, max_length=180),
        ),
    ]
