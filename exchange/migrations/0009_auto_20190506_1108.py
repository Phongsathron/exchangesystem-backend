# Generated by Django 2.2.1 on 2019-05-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0008_delete_exchange'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deal',
            old_name='score',
            new_name='offerer_score',
        ),
        migrations.AddField(
            model_name='deal',
            name='owner_score',
            field=models.IntegerField(null=True),
        ),
    ]
