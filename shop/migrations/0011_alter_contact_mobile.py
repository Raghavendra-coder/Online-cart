# Generated by Django 3.2.4 on 2021-06-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(default=''),
        ),
    ]
