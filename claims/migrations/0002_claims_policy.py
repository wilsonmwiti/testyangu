# Generated by Django 3.1 on 2021-06-30 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('claims', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='claims',
            name='policy',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Policy'),
        ),
    ]