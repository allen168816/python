# Generated by Django 2.2.1 on 2019-05-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20190520_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useradvice',
            name='advices',
            field=models.CharField(max_length=255, verbose_name='用户建议'),
        ),
    ]
