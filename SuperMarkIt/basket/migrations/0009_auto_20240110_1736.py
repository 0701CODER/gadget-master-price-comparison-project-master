# Generated by Django 3.1 on 2024-01-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0008_auto_20240109_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='total_amazon',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='total_flipkart',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='total_snapdeal',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='basketitem',
            name='product_total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]