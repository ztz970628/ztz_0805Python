# Generated by Django 2.1.8 on 2019-10-31 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quser',
            name='identity',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
