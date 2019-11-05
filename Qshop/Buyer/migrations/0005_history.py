# Generated by Django 2.1.8 on 2019-11-05 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0004_auto_20191105_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=32)),
                ('goods_id', models.IntegerField()),
                ('goods_name', models.TextField()),
                ('goods_price', models.FloatField()),
                ('goods_picture', models.TextField()),
            ],
        ),
    ]
