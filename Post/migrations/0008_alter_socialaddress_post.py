# Generated by Django 5.1.5 on 2025-02-03 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0007_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaddress',
            name='Post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Social', to='Post.post'),
        ),
    ]
