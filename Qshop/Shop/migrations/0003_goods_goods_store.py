# Generated by Django 2.1.8 on 2019-10-31 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QUser', '0002_quser_identity'),
        ('Shop', '0002_auto_20191030_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_store',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='QUser.Quser'),
            preserve_default=False,
        ),
    ]