# Generated by Django 2.0.12 on 2019-07-05 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snmphostdata',
            options={'ordering': ('-date_created',), 'verbose_name': 'SNMP部件监控数据'},
        ),
    ]
