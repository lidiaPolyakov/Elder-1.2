# Generated by Django 4.1.4 on 2023-03-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore',
            name='creation_time',
            field=models.CharField(default='17:50:35', max_length=200),
        ),
    ]
