# Generated by Django 3.1.5 on 2021-12-22 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0006_about_copywright'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='date_created',
            new_name='date_sent',
        ),
    ]