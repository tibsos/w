# Generated by Django 4.1.2 on 2022-11-03 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='N',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4)),
                ('t', models.CharField(blank=True, max_length=300)),
                ('c', models.TextField(blank=True, max_length=1000000)),
                ('p', models.BooleanField(default=False)),
                ('ca', models.DateTimeField(auto_now_add=True)),
                ('ua', models.DateTimeField(auto_now=True)),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['p', '-ua'],
            },
        ),
    ]