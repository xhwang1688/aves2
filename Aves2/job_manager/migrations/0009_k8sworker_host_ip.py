# Generated by Django 2.2 on 2020-03-13 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_manager', '0008_auto_20200308_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='k8sworker',
            name='host_ip',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
    ]