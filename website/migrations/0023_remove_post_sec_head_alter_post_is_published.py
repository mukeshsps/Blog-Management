# Generated by Django 4.0.3 on 2022-06-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_post_sec_head'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sec_head',
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]