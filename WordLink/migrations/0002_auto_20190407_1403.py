# Generated by Django 2.1.7 on 2019-04-07 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WordLink', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word_link',
            name='user_id',
        ),
        migrations.AddField(
            model_name='word_link',
            name='username',
            field=models.CharField(default='not set', max_length=100),
        ),
        migrations.AlterField(
            model_name='word_link',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
