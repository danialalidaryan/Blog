# Generated by Django 5.1.5 on 2025-02-04 14:47

import Post.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.post'),
        ),
    ]
