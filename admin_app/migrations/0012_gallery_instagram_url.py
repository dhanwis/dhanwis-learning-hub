# Generated by Django 4.1 on 2024-07-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0011_placement_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
