# Generated by Django 3.1.4 on 2021-01-07 11:34

from django.db import migrations
import webpage_proj.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', webpage_proj.accounts.models.CustomUserManager()),
            ],
        ),
    ]