# Generated by Django 4.2.3 on 2023-07-29 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('c_validator', '0003_certificate_signature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='verification_code',
        ),
    ]