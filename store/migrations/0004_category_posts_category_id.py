# Generated by Django 5.0.6 on 2024-06-01 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_posts_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.category'),
        ),
    ]