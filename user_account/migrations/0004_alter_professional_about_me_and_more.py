# Generated by Django 4.2.6 on 2023-11-06 08:55

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app_platform', '0004_remove_city_postal_code_remove_city_status_and_more'),
        ('user_account', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='about_me',
            field=models.TextField(null=True, verbose_name='about me'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='base_address',
            field=models.ForeignKey(help_text='Specify the central location, or origin.', on_delete=django.db.models.deletion.DO_NOTHING, related_name='professional_base_address', to='app_platform.city'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='service_area_radius',
            field=models.IntegerField(blank=True, help_text='Define a specific distance within which you are willing to provide your services.', null=True, verbose_name='service area radius'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='PH'),
        ),
    ]
