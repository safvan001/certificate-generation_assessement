# Generated by Django 4.2.3 on 2023-07-19 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_validator', '0002_rename_content_certificate_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='signature',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]