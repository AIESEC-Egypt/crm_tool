# Generated by Django 3.1.1 on 2020-10-21 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0013_auto_20201020_0250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='completed_atleast_one_membership_cycle',
            new_name='completed_at_least_one_membership_cycle',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='managed_applcations_count',
            new_name='managed_applications_count',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='number_of_touchpoints_attended',
            new_name='number_of_touch_points_attended',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='number_of_touchpoints_hosted',
            new_name='number_of_touch_points_hosted',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='number_of_touchpoints_required_to_attend',
            new_name='number_of_touch_points_required_to_attend',
        ),
        migrations.RemoveField(
            model_name='member',
            name='touchpoints',
        ),
    ]
