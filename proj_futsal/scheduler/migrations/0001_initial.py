# Generated by Django 4.1 on 2022-11-13 01:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_date', models.DateField(default=datetime.datetime(2022, 11, 13, 10, 29, 41, 27530))),
                ('event_start', models.TimeField(default=datetime.datetime(2022, 11, 13, 10, 29, 41, 27530))),
                ('event_end', models.TimeField(default=datetime.datetime(2022, 11, 13, 10, 29, 41, 27530))),
                ('event_created', models.DateTimeField(auto_now_add=True)),
                ('event_updated', models.DateTimeField(auto_now=True)),
                ('event_comment', models.TextField()),
                ('event_status', models.CharField(choices=[('CO', 'Confirmed'), ('UC', 'Unconfirmed'), ('CA', 'Cancelled')], max_length=2)),
            ],
            options={
                'ordering': ['event_date', 'event_start'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('player_status', models.CharField(choices=[('PL', 'Player'), ('WA', 'Watching')], max_length=2)),
                ('attendance_status', models.CharField(choices=[('CO', 'Confirmed'), ('MB', 'Maybe'), ('NO', 'Will not attend')], max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relevant_event_name', to='scheduler.event')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
