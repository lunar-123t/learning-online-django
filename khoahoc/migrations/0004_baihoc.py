# Generated by Django 4.1.1 on 2022-10-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khoahoc', '0003_levelkhoahoc_monhoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaiHoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_bai', models.CharField(max_length=50)),
                ('url_anh', models.CharField(max_length=100)),
                ('thoi_luong', models.CharField(max_length=100)),
                ('video_id', models.IntegerField()),
                ('oder', models.CharField(max_length=50)),
            ],
        ),
    ]