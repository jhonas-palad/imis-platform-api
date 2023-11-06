# Generated by Django 4.2.6 on 2023-11-03 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_platform', '0003_state_remove_address_postal_code_and_more'),
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type', models.CharField(choices=[('LOCAL', 'Local'), ('ANY', 'Anywhere')], default='LOCAL', max_length=15, verbose_name='location type')),
                ('service_area_radius', models.IntegerField(blank=True, help_text='Service Area Radius allows you to define a specific distance within which you are willing to provide your services.', null=True, verbose_name='service area radius')),
                ('about_me', models.TextField(verbose_name='about me')),
                ('base_address', models.ForeignKey(help_text='Specify the central location, or origin, from which pro are willing to provide their services.', on_delete=django.db.models.deletion.DO_NOTHING, related_name='professional_base_address', to='app_platform.city')),
                ('service_area', models.ManyToManyField(related_name='professional_service_area', to='app_platform.city')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
