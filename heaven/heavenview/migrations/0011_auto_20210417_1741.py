# Generated by Django 3.1.6 on 2021-04-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heavenview', '0010_auto_20210417_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.IntegerField(null=True),
        ),
    ]
