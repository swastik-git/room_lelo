# Generated by Django 2.2.6 on 2019-11-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_lelo', '0002_auto_20191108_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='facility',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
