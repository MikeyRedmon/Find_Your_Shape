# Generated by Django 3.2.18 on 2023-03-08 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_ptclasses'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpinClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=10)),
                ('time', models.DateTimeField(max_length=10)),
            ],
        ),
    ]