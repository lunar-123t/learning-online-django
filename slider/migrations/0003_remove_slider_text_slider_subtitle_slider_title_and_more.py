# Generated by Django 4.1.1 on 2022-10-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_slider_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='text',
        ),
        migrations.AddField(
            model_name='slider',
            name='subtitle',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
