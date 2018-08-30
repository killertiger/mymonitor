# Generated by Django 2.1 on 2018-08-30 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmonitor', '0003_auto_20180830_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connection',
            name='connection_string',
        ),
        migrations.AddField(
            model_name='connection',
            name='host',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='connection',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='connection',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]