# Generated by Django 3.1.6 on 2021-02-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlmtools', '0004_auto_20210219_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketernode',
            name='node_cut',
            field=models.DecimalField(decimal_places=2, default=50.0, help_text='How much does this node get', max_digits=5),
        ),
    ]
