# Generated by Django 4.0.3 on 2022-06-15 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_viewcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_details',
            name='category',
        ),
    ]
