# Generated by Django 4.2.3 on 2023-07-19 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('c_validator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='content',
            new_name='subtitle',
        ),
    ]