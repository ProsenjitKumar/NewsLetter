# Generated by Django 2.1.3 on 2018-11-17 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsltters', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletteruser',
            old_name='date_adaded',
            new_name='date_added',
        ),
    ]
