# Generated by Django 5.1.1 on 2024-10-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aipc_diagnosis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='url',
            field=models.URLField(max_length=1000),
        ),
    ]