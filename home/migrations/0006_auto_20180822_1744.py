# Generated by Django 2.0.6 on 2018-08-22 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180822_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='id',
        ),
        migrations.AddField(
            model_name='article',
            name='pic_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
