# Generated by Django 4.0.4 on 2022-05-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_rename_instructor_image_row1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_row2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
