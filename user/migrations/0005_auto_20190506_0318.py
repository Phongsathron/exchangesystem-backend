# Generated by Django 2.2.1 on 2019-05-06 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190506_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(null=True, upload_to='profile'),
        ),
    ]
