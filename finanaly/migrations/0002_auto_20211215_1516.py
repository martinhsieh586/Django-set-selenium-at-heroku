# Generated by Django 3.2.9 on 2021-12-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanaly', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='useremail',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userpassword',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
