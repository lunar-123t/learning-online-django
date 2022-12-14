# Generated by Django 4.1.1 on 2022-10-30 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_rename_mess_chat_mess_text_remove_chat_receiver_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='mess_text',
            new_name='message_text',
        ),
        migrations.AlterField(
            model_name='chat',
            name='is_my_messages',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='message_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 30, 15, 46, 18, 656699)),
        ),
    ]
