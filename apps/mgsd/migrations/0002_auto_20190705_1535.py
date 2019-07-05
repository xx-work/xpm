# Generated by Django 2.0.12 on 2019-07-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgsd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditpolicycentralizedmanagement',
            name='systempolicycentralizedmanagement_ptr',
        ),
        migrations.RemoveField(
            model_name='securitypolicycentralizedmanagement',
            name='systempolicycentralizedmanagement_ptr',
        ),
        migrations.RemoveField(
            model_name='systempolicycentralizedmanagement',
            name='sys_dbackup',
        ),
        migrations.RemoveField(
            model_name='systempolicycentralizedmanagement',
            name='sys_except_handle',
        ),
        migrations.RemoveField(
            model_name='systempolicycentralizedmanagement',
            name='sys_stat',
        ),
        migrations.RemoveField(
            model_name='systempolicycentralizedmanagement',
            name='sys_user',
        ),
        migrations.AddField(
            model_name='systempolicycentralizedmanagement',
            name='sources',
            field=models.TextField(blank=True, verbose_name='连接的资源情况'),
        ),
        migrations.AlterModelTable(
            name='systempolicycentralizedmanagement',
            table='system_policy_cen_mg',
        ),
        migrations.DeleteModel(
            name='AuditPolicyCentralizedManagement',
        ),
        migrations.DeleteModel(
            name='SecurityPolicyCentralizedManagement',
        ),
    ]
