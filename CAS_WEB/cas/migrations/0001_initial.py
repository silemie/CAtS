# Generated by Django 2.1.7 on 2019-06-14 20:06

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
            name='Control',
            fields=[
                ('cid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('gid', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=100)),
                ('parameters', models.TextField(blank=True, null=True)),
                ('properties', models.TextField(blank=True, null=True)),
                ('links', models.TextField(blank=True, null=True)),
                ('parts', models.TextField(blank=True, null=True)),
                ('classinfo', models.CharField(blank=True, max_length=32, null=True)),
                ('pid', models.CharField(blank=True, max_length=10, null=True)),
                ('high', models.BooleanField()),
                ('moderate', models.BooleanField()),
                ('low', models.BooleanField()),
            ],
            options={
                'db_table': 'control',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=600, null=True)),
                ('created_time', models.DateTimeField()),
                ('updated_time', models.DateTimeField()),
                ('control', models.ManyToManyField(to='cas.Control')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
