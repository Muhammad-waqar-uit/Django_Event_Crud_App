# Generated by Django 4.0.1 on 2022-02-09 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myProject', '0002_rename_venue_venue_ven'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='Ven',
            new_name='venues',
        ),
    ]