# Generated by Django 4.0.4 on 2022-05-16 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_singlepost_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Singlepost_Post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='first_text',
        ),
    ]
