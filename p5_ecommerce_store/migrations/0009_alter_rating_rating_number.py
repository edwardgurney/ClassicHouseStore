# Generated by Django 3.2 on 2022-04-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p5_ecommerce_store', '0008_auto_20220412_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating_number',
            field=models.IntegerField(default=0),
        ),
    ]
