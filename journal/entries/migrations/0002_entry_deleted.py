# Generated by Django 5.1.2 on 2024-11-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]