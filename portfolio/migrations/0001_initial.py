# Generated by Django 4.1.7 on 2024-01-18 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(upload_to='projects/thumbnails/')),
                ('description', models.TextField()),
            ],
        ),
    ]
