# Generated by Django 3.1.1 on 2020-10-20 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm', '0005_auto_20201020_0238'),
        ('general', '0011_auto_20201019_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='productivity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='retention',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='team_standards',
            field=models.ManyToManyField(blank=True, null=True, to='tm.TeamStandards'),
        ),
    ]
