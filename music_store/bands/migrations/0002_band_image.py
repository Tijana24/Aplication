# Generated by Django 3.1.5 on 2021-01-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='image',
            field=models.URLField(default='https://img.etimg.com/thumb/msid-73612807,width-650,imgsize-212384,,resizemode-4,quality-100/vinyl-records_istock.jpg'),
        ),
    ]
