# Generated by Django 3.1 on 2024-01-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0007_auto_20240109_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='total_amazon',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='total_flipkart',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='total_snapdeal',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
    ]
