# Generated by Django 2.2.2 on 2022-02-25 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(blank=True),
        ),
    ]