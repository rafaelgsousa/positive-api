# Generated by Django 5.0.6 on 2024-06-28 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positive', '0006_alter_customuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=1, null=True, verbose_name='last name'),
        ),
    ]
