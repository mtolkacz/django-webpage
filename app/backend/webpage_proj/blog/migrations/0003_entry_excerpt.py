# Generated by Django 3.1.4 on 2021-01-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210113_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='excerpt',
            field=models.TextField(null=True),
        ),
    ]