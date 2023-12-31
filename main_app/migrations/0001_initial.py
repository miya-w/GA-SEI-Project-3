# Generated by Django 4.2.4 on 2023-08-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=200)),
                ('suburb', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=3)),
                ('postcode', models.IntegerField()),
                ('details', models.TextField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
