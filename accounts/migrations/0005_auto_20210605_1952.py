# Generated by Django 3.2.4 on 2021-06-05 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210605_1939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='files',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='files',
            name='name',
        ),
    ]
