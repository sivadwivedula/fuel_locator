# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 04:53
from __future__ import unicode_literals

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
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('cr_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticeforowner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('cr_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.CharField(blank=True, max_length=45)),
                ('pname', models.CharField(max_length=45)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10, null=True)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10, null=True)),
                ('contact_no', models.BigIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=70)),
                ('opening_time', models.TimeField(blank=True, null=True)),
                ('closing_time', models.TimeField(blank=True, null=True)),
                ('near_by_highway', models.NullBooleanField()),
                ('website', models.CharField(blank=True, max_length=45, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('visits', models.BigIntegerField(blank=True, null=True)),
                ('rating', models.BigIntegerField(blank=True, null=True)),
                ('price_petrol', models.FloatField(blank=True, null=True)),
                ('price_diesel', models.FloatField(blank=True, null=True)),
                ('atm', models.NullBooleanField()),
                ('toilets', models.NullBooleanField()),
                ('air', models.NullBooleanField()),
                ('first_aid', models.NullBooleanField()),
                ('water', models.NullBooleanField()),
                ('rest_room', models.NullBooleanField()),
                ('card_accepted', models.NullBooleanField()),
                ('last_updated', models.DateField(null=True)),
                ('petrol', models.NullBooleanField()),
                ('diesel', models.NullBooleanField()),
                ('verified', models.NullBooleanField()),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
