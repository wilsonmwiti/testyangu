# Generated by Django 3.1 on 2021-06-12 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentLeads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AgentIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100, verbose_name='Link(Use for referral)')),
                ('id_front', models.FileField(upload_to='user/agent/id', verbose_name='National ID Front')),
                ('id_back', models.FileField(upload_to='user/agent/id', verbose_name='National ID Back')),
                ('ira', models.FileField(upload_to='user/agent/ira', verbose_name='IRA Licence')),
                ('profile', models.FileField(upload_to='user/agent/profile', verbose_name='Profile Image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Agent')),
            ],
            options={
                'db_table': 'Agent Identity Information',
            },
        ),
        migrations.CreateModel(
            name='AgentAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mpesa', models.CharField(blank=True, max_length=50, verbose_name='Mpesa')),
                ('bank_name', models.CharField(blank=True, max_length=50, verbose_name='Bank Name')),
                ('bank_branch', models.CharField(blank=True, max_length=50, verbose_name='Bank Branch')),
                ('account_number', models.CharField(blank=True, max_length=50, verbose_name='Bank Account Number')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Agent')),
            ],
            options={
                'db_table': 'Agent Bank Account Information',
            },
        ),
    ]