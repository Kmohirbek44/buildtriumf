# Generated by Django 4.1 on 2022-08-29 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_category_id_alter_city_id_alter_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='company_name',
        ),
    ]
