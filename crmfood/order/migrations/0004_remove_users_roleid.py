# Generated by Django 2.1.3 on 2018-11-16 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20181116_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='roleid',
        ),
    ]
