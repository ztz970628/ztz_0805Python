# Generated by Django 2.1.8 on 2019-11-05 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_auto_20191031_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QUser.Quser'),
        ),
    ]
