# Generated by Django 3.1.2 on 2020-12-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20201220_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='', max_length=10),
        ),
    ]
