# Generated by Django 4.2.3 on 2023-07-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CastoonnApp', '0003_email_validation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_validation',
            name='email_temp',
            field=models.EmailField(max_length=254),
        ),
    ]