# Generated by Django 3.1.1 on 2020-10-18 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_auto_20201018_0512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='completed_one_membership_cycle',
            new_name='completed_atleast_one_membership_cycle',
        ),
    ]
