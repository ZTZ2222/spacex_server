# Generated by Django 4.2.3 on 2023-07-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacex_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='name',
            field=models.CharField(default='Link', max_length=10),
        ),
        migrations.AddField(
            model_name='statsitem',
            name='name',
            field=models.CharField(default='Block', max_length=10),
        ),
    ]
