# Generated by Django 5.0.6 on 2024-06-08 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
