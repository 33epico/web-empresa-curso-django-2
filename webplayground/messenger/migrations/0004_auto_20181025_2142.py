# Generated by Django 2.0.2 on 2018-10-25 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_auto_20181025_2136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-updated']},
        ),
    ]
