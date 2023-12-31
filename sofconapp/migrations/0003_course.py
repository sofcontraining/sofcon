# Generated by Django 4.2 on 2023-09-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sofconapp', '0002_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=255)),
                ('csummary', models.TextField()),
                ('cimg', models.ImageField(upload_to='courseimages')),
                ('heading', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=500)),
            ],
        ),
    ]
