# Generated by Django 3.2.5 on 2021-08-04 19:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('product', models.TextField(null=True)),
                ('role', models.TextField(null=True)),
                ('pdf', models.FileField(upload_to='media/pdf')),
                ('cover', models.ImageField(upload_to='media/covers')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
