# Generated by Django 3.1 on 2024-01-09 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0006_auto_20191115_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='total_morrisons',
            new_name='total_amazon',
        ),
        migrations.RenameField(
            model_name='basket',
            old_name='total_sainsburys',
            new_name='total_flipkart',
        ),
        migrations.RenameField(
            model_name='basket',
            old_name='total_tesco',
            new_name='total_snapdeal',
        ),
    ]