# Generated by Django 4.1.1 on 2022-11-13 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_alter_chat_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='message_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 13, 15, 23, 39, 557233)),
        ),
    ]
