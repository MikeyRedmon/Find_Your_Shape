# Generated by Django 3.2.18 on 2023-02-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiitbook',
            name='name',
            field=models.CharField(default='High Intensitiy Interval Training', max_length=10),
            preserve_default=False,
        ),
    ]
