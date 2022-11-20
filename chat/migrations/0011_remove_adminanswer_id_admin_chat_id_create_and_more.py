# Generated by Django 4.1.1 on 2022-11-13 07:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_adminanswer_id_admin_alter_chat_message_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminanswer',
            name='id_admin',
        ),
        migrations.AddField(
            model_name='chat',
            name='id_create',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.adminanswer'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='message_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 13, 14, 54, 51, 354830)),
        ),
    ]