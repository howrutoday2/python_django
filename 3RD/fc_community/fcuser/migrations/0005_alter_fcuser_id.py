# Generated by Django 4.0.2 on 2022-04-01 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0004_auto_20220401_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
