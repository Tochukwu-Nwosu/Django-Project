# Generated by Django 4.0.4 on 2022-05-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_image_row2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vertical_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
