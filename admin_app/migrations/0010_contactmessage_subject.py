# Generated by Django 4.1 on 2024-07-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0009_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]