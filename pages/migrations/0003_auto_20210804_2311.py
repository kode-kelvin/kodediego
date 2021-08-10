# Generated by Django 3.2.5 on 2021-08-04 23:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_project_demo_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='pages.Tag'),
        ),
    ]