# Generated by Django 2.2.10 on 2021-02-11 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_auto_20210211_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firmuser',
            old_name='firmdetails',
            new_name='firmname',
        ),
    ]
