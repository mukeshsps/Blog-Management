# Generated by Django 4.0.3 on 2022-06-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_post_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(),
        ),
    ]