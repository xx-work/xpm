# Generated by Django 2.0.12 on 2019-06-25 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snmphostdata',
            options={'ordering': ('date_created',), 'verbose_name': 'SNMP部件监控数据'},
        ),
        migrations.AlterField(
            model_name='snmphostdata',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='监控时间'),
        ),
    ]
