# Generated by Django 3.2.9 on 2022-01-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanaly', '0006_alter_bussinessinfo_searchurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='bussinessinfo',
            name='detailcapture',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bussinessinfo',
            name='namecapture',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bussinessinfo',
            name='pricecapture',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
