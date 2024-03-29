# Generated by Django 3.1.1 on 2020-10-19 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0011_auto_20201019_1322'),
        ('tm', '0002_delete_membership_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pipeline_type', models.CharField(choices=[('LCP', 'Local Committee President'), ('LCVP', 'Local Committee Vice President'), ('TL', 'Team Leader'), ('COO', 'Coordinator'), ('NA', 'Not Interested')], default='Not Interested', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='TeamStandards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Nes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommending_aiesec_to_a_friend', models.IntegerField(blank=True, default=0, null=True)),
                ('tl_satisfaction', models.IntegerField(blank=True, default=0, null=True)),
                ('percentage_of_goal_achievement', models.IntegerField(blank=True, default=0, null=True)),
                ('rating_explaination', models.TextField(blank=True, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.department')),
                ('lc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.entity')),
                ('member_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.member')),
                ('pipeline', models.ManyToManyField(blank=True, default=0, null=True, to='tm.Pipeline')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.role')),
            ],
        ),
    ]
