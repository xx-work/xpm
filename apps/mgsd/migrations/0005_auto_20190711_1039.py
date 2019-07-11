# Generated by Django 2.0.12 on 2019-07-11 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgsd', '0004_auto_20190711_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordqueryset',
            name='type',
            field=models.CharField(default='password', max_length=55, verbose_name='应用强度类型'),
        ),
        migrations.AlterField(
            model_name='passwordqueryset',
            name='desc',
            field=models.CharField(default='字母数字在8-16范围内', max_length=55, verbose_name='密码描述'),
        ),
        migrations.AlterField(
            model_name='passwordqueryset',
            name='name',
            field=models.CharField(default='基本强度密码', max_length=55, verbose_name='密码名称'),
        ),
        migrations.AlterField(
            model_name='passwordqueryset',
            name='rgx',
            field=models.CharField(default='[\\d\\w_]{8,16}', max_length=255, verbose_name='密码正则'),
        ),
    ]
