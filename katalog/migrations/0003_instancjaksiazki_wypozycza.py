# Generated by Django 2.1.5 on 2021-05-29 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('katalog', '0002_instancjaksiazki_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='instancjaksiazki',
            name='wypozycza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
