# Generated by Django 5.0.2 on 2024-12-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0005_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
