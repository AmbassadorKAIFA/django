# Generated by Django 4.1.4 on 2022-12-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0004_alter_table_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='booking',
            field=models.BooleanField(default=False),
        ),
    ]