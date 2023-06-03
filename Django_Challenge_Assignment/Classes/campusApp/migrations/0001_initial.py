# Generated by Django 4.2.1 on 2023-06-03 02:19

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus_name', models.CharField(blank=True, default='', max_length=60)),
                ('state', models.CharField(blank=True, default='', max_length=2)),
                ('campus_id', models.IntegerField(blank=True, default=None)),
            ],
            options={
                'verbose_name': 'University Campus',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
