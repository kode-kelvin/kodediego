# Generated by Django 3.2.5 on 2021-08-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210804_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='source_code',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
