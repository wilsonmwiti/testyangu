# Generated by Django 3.1 on 2021-05-31 13:22

import ckeditor.fields
import datetime
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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=40)),
                ('text', ckeditor.fields.RichTextField()),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('claps', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='website/blog')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]