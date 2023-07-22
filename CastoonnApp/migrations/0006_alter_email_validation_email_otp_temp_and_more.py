# Generated by Django 4.2.3 on 2023-07-22 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CastoonnApp', '0005_alter_user_registration_email_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_validation',
            name='email_otp_temp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Creator_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(blank=True, upload_to='photos/')),
                ('firstname', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('phonenumber', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('marital_status', models.CharField(blank=True, max_length=255, null=True)),
                ('profection', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('interests', models.TextField(blank=True, null=True)),
                ('hobbies', models.TextField(blank=True, null=True)),
                ('passions', models.TextField(blank=True, null=True)),
                ('goals', models.TextField(blank=True, null=True)),
                ('achievements', models.TextField(blank=True, null=True)),
                ('social_media_links', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('awards', models.TextField(blank=True, null=True)),
                ('more_abt_u', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CastoonnApp.user_registration')),
            ],
        ),
    ]
