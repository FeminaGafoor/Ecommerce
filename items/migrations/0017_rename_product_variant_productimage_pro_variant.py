# Generated by Django 4.2.6 on 2023-10-20 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0016_remove_productimage_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='product_variant',
            new_name='pro_variant',
        ),
    ]
