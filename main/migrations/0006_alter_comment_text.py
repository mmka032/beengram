# Generated by Django 4.0rc1 on 2025-01-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
