# Generated by Django 3.2.9 on 2022-01-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanaly', '0004_alter_bussinessinfo_searchurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bussinessinfo',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
