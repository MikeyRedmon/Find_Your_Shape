# Generated by Django 3.2.18 on 2023-02-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_hiitbook_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiitbook',
            name='spaces',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
