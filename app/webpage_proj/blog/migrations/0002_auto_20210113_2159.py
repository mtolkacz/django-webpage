# Generated by Django 3.1.4 on 2021-01-13 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AddField(
            model_name='entry',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=250, unique_for_date='pub_date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]
