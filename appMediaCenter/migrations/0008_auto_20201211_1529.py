# Generated by Django 3.1.4 on 2020-12-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMediaCenter', '0007_auto_20201211_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='folder',
            field=models.CharField(max_length=20),
        ),
    ]
