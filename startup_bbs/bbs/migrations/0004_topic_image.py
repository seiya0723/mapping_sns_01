# Generated by Django 3.2.12 on 2022-05-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_topic_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bbs/topic/image/', verbose_name='画像'),
        ),
    ]
