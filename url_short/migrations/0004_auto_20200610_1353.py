# Generated by Django 3.0.7 on 2020-06-10 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0003_auto_20200610_1110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlshortdb',
            old_name='long_url',
            new_name='long_url_db',
        ),
        migrations.RenameField(
            model_name='urlshortdb',
            old_name='shorted_url',
            new_name='shorted_url_db',
        ),
    ]
