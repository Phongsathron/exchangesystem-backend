# Generated by Django 2.2.1 on 2019-05-03 08:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_product_picture_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_picture',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
