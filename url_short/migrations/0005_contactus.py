# Generated by Django 3.0.7 on 2020-06-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0004_auto_20200610_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=40)),
                ('messege', models.CharField(max_length=2000)),
            ],
        ),
    ]
