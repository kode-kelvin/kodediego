# Generated by Django 3.2.5 on 2021-08-06 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_project_source_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='worktype',
            field=models.CharField(blank=True, choices=[('software dev', 'Software Dev'), ('product design', 'Product Design')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/pdf'),
        ),
    ]
