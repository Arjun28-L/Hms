# Generated by Django 5.0.3 on 2024-05-19 12:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0007_alter_appointment_time_slot'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='Userpics')),
                ('address', models.CharField(max_length=40)),
                ('shift', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon')], default='Morning', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms', models.TextField()),
                ('prescription', models.TextField()),
                ('Advice', models.TextField()),
                ('app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Appointment.appointment')),
            ],
        ),
    ]