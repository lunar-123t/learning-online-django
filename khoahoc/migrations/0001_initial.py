# Generated by Django 4.1.1 on 2022-09-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Khoahoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenkhoahoc', models.CharField(max_length=50)),
                ('urlanh', models.CharField(max_length=100)),
            ],
        ),
    ]