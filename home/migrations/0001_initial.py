# Generated by Django 3.2.18 on 2023-03-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hiitbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('focus', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='hittclasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('trainer', models.CharField(max_length=10)),
                ('focus', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PtClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('trainer', models.CharField(max_length=10)),
                ('focus', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SpinClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=10)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
