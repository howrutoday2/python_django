# Generated by Django 2.1.5 on 2022-04-01 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcuser.Fcuser', verbose_name='작성자'),
        ),
    ]
