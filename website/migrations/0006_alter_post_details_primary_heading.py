# Generated by Django 4.0.3 on 2022-05-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_post_details_posted_on_post_details_primary_heading_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_details',
            name='primary_heading',
            field=models.CharField(default='', max_length=100),
        ),
    ]
