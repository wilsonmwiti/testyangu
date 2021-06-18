# Generated by Django 3.1 on 2021-05-31 13:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsBackground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_bg_image', models.ImageField(upload_to='website/account')),
                ('sign_up_bg_image', models.ImageField(upload_to='website/account')),
            ],
            options={
                'db_table': 'Account login and sign-up backgrounds',
            },
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='website/base', verbose_name='Logo image cropped and without background')),
                ('icon', models.ImageField(upload_to='website/base', verbose_name='Logo Icon')),
                ('facebook', models.URLField(blank=True, max_length=50, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, max_length=50, verbose_name='Twitter')),
                ('linkedin', models.URLField(blank=True, max_length=50, verbose_name='LinkedIn')),
                ('youtube', models.URLField(blank=True, max_length=50, verbose_name='Youtube')),
                ('phone_number', models.CharField(blank=True, max_length=14, verbose_name='Phone number')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('footer_advert', models.ImageField(upload_to='website/base', verbose_name='Footer image advert bellow newsletter')),
            ],
            options={
                'db_table': 'Elimusmart links and resources',
            },
        ),
        migrations.CreateModel(
            name='BusinessSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50, verbose_name='Heading')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('first_point', models.CharField(max_length=50, verbose_name='Second point')),
                ('second_point', models.CharField(blank=True, max_length=50, verbose_name='First point')),
                ('image', models.ImageField(upload_to='website/home', verbose_name='Image')),
            ],
            options={
                'db_table': 'Business section',
            },
        ),
        migrations.CreateModel(
            name='ClientsFeedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='website/home/clients', verbose_name="Client's profile picture 80 by 80")),
                ('content', ckeditor.fields.RichTextField(verbose_name='What they say about elimusmart')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('job_description', models.CharField(blank=True, max_length=70, verbose_name='Job description')),
            ],
            options={
                'db_table': 'Testimonials',
            },
        ),
        migrations.CreateModel(
            name='ContactUsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image', models.ImageField(upload_to='website/contact')),
                ('office_address', models.CharField(blank=True, max_length=150, verbose_name='Office address')),
                ('primary_phone', models.CharField(max_length=50, verbose_name='Primary phone number')),
                ('secondary_phone', models.CharField(blank=True, max_length=50, verbose_name='Secondary phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('website', models.URLField(blank=True, verbose_name='Website')),
                ('map_location', models.CharField(blank=True, max_length=500, verbose_name='Google map location')),
            ],
            options={
                'db_table': 'Contact us information',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'db_table': 'FAQ ',
            },
        ),
        migrations.CreateModel(
            name='FAQImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='website/home', verbose_name='image')),
            ],
            options={
                'db_table': 'FAQ image',
            },
        ),
        migrations.CreateModel(
            name='HomeAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_title', models.CharField(blank=True, max_length=50, verbose_name='Title')),
                ('primary_content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('mission', ckeditor.fields.RichTextField(verbose_name='Our mission')),
                ('first_image', models.ImageField(upload_to='website/home', verbose_name='Image size 370 by 348')),
                ('second_image', models.ImageField(upload_to='website/home', verbose_name='Image size 370 by 471')),
            ],
            options={
                'db_table': 'Home about us',
            },
        ),
        migrations.CreateModel(
            name='HomeCarouselOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_heading', models.CharField(blank=True, max_length=50, verbose_name='Main heading')),
                ('main_content', models.CharField(blank=True, max_length=50, verbose_name='Main content')),
                ('secondary_heading', models.CharField(blank=True, max_length=50, verbose_name='Secondary heading')),
                ('secondary_content', models.CharField(blank=True, max_length=50, verbose_name='Secondary content')),
                ('bg_image', models.ImageField(upload_to='website/home', verbose_name='Background image')),
            ],
            options={
                'db_table': 'First home page carousel',
            },
        ),
        migrations.CreateModel(
            name='HomeCarouselTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_heading', models.CharField(blank=True, max_length=50, verbose_name='Main heading')),
                ('main_content', models.CharField(blank=True, max_length=50, verbose_name='Main content')),
                ('secondary_heading', models.CharField(blank=True, max_length=50, verbose_name='Secondary heading')),
                ('secondary_content', models.CharField(blank=True, max_length=50, verbose_name='Secondary content')),
                ('bg_image', models.ImageField(upload_to='website/home', verbose_name='Background image')),
            ],
            options={
                'db_table': 'Second Home page carousel one',
            },
        ),
        migrations.CreateModel(
            name='MainAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_bg', models.ImageField(upload_to='website/about', verbose_name='Header background')),
                ('image', models.ImageField(upload_to='website/about', verbose_name='Image 550 by 542')),
                ('main_heading', models.CharField(max_length=50, verbose_name='Main heading')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('action_point_one', models.CharField(max_length=50, verbose_name='Action point one')),
                ('action_point_two', models.CharField(max_length=50, verbose_name='Action point two')),
                ('action_point_three', models.CharField(max_length=50, verbose_name='Action point three')),
                ('action_point_four', models.CharField(max_length=50, verbose_name='Action point four')),
            ],
            options={
                'db_table': 'Main about us',
            },
        ),
        migrations.CreateModel(
            name='OurAdvantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('icon', models.CharField(blank=True, max_length=50, verbose_name='Icon(please use favicon)')),
            ],
            options={
                'db_table': 'Our Insurance advantage',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('content', models.CharField(max_length=70, verbose_name='Content')),
                ('phone', models.CharField(max_length=12, verbose_name='Phone')),
            ],
            options={
                'db_table': 'Get a quote ',
            },
        ),
        migrations.CreateModel(
            name='WhatWeDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='website/about', verbose_name='Image')),
                ('main_heading', models.CharField(max_length=50, verbose_name='Small one word Heading')),
                ('small_heading', models.CharField(max_length=50, verbose_name='Big heading ')),
            ],
            options={
                'db_table': 'What our cover entails',
            },
        ),
    ]
