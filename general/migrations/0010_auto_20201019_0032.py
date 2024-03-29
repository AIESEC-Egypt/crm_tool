# Generated by Django 3.1.1 on 2020-10-18 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0009_auto_20201018_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperationalGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(choices=[('1', 'Sign UPs'), ('2', 'Applied'), ('3', 'Accepted'), ('4', 'Approved'), ('5', 'Realized'), ('6', 'Finished'), ('7', 'Complete'), ('XX', 'Choose a type')], default='XX', max_length=2)),
                ('number', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='number_of_touchpoints_attended',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='number_of_touchpoints_hosted',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='number_of_touchpoints_required_to_attend',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='hierarchy',
            field=models.CharField(choices=[('1', 'Member'), ('2', 'Coordinator'), ('3', 'LCVP'), ('4', 'LCP'), ('5', 'EDT'), ('6', 'EDT TL'), ('7', 'RST'), ('8', 'GST'), ('9', 'ECB Chair'), ('10', 'ECB Director'), ('11', 'ECB Member'), ('12', 'EFB Chair'), ('13', 'EFB Director'), ('14', 'EFB Member'), ('15', 'MCVP'), ('16', 'MCP'), ('17', 'Alumnus'), ('xx', 'Other')], default='Other', max_length=2),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_status',
            field=models.CharField(choices=[('1', 'Active Member'), ('2', 'Member on IXP'), ('3', 'Resigned'), ('4', 'Dismissed'), ('5', 'Under Probation'), ('6', 'Alumnus')], default='Active Member', max_length=1),
        ),
        migrations.RemoveField(
            model_name='member',
            name='role',
        ),
        migrations.AddField(
            model_name='member',
            name='role',
            field=models.ManyToManyField(blank=True, null=True, to='general.Role'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TouchPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_id', models.IntegerField(blank=True, default=0, null=True)),
                ('start_date_time', models.DateTimeField(blank=True, null=True)),
                ('end_date_time', models.DateTimeField(blank=True, null=True)),
                ('meeting_name', models.CharField(blank=True, default=0, max_length=250, null=True)),
                ('meeting_type', models.CharField(choices=[('1', 'National Conference'), ('2', 'Local Conference'), ('3', 'LCM'), ('4', 'MCM'), ('5', 'Comission Meeting'), ('6', 'Functional Visit'), ('7', 'OD Visit'), ('8', 'o2o'), ('9', 'Comission Meeting'), ('10', 'Functional Meeting'), ('11', 'TLs Meeting'), ('12', 'EB Meeting'), ('13', 'Management Team Meeting'), ('14', 'OD Meeting'), ('15', 'OPS Meeting'), ('16', 'Brand Meeting'), ('17', 'Finance Meeting'), ('18', 'EDTs Meeting'), ('19', 'IR Meeting'), ('20', 'LC Outing'), ('21', 'Teamdays'), ('XX', 'Other')], default='Other', max_length=2)),
                ('audience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.role')),
                ('meeting_host_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.entity')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='operational_goals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.operationalgoal'),
        ),
        migrations.AddField(
            model_name='member',
            name='touchpoints',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='general.touchpoints'),
        ),
    ]
