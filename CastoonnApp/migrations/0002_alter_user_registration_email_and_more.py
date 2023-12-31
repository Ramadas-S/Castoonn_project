# Generated by Django 4.2.3 on 2023-07-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CastoonnApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_registration',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='email_otp',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
    ]
