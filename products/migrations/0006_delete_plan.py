# Generated by Django 3.2 on 2022-01-24 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_plan_equipment_needed'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Plan',
        ),
    ]