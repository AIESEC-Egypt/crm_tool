# Generated by Django 3.1.1 on 2020-10-19 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0011_auto_20201019_1322'),
        ('tm', '0003_nes_pipeline_teamstandards'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_lda', models.BooleanField(blank=True, default=False, null=True)),
                ('pdp', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamCreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transition', models.BooleanField(blank=True, default=False, null=True)),
                ('competence', models.BooleanField(blank=True, default=False, null=True)),
                ('team_rules', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_purpose', models.BooleanField(blank=True, default=False, null=True)),
                ('goals', models.BooleanField(blank=True, default=False, null=True)),
                ('strategies', models.BooleanField(blank=True, default=False, null=True)),
                ('timeline', models.BooleanField(blank=True, default=False, null=True)),
                ('jds', models.BooleanField(blank=True, default=False, null=True)),
                ('budget', models.BooleanField(blank=True, default=False, null=True)),
                ('team_development', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='nes',
            options={'verbose_name': 'NES', 'verbose_name_plural': 'NES'},
        ),
        migrations.AlterModelOptions(
            name='teamstandards',
            options={'verbose_name': 'Team Standards', 'verbose_name_plural': 'Team Standards'},
        ),
        migrations.RenameField(
            model_name='nes',
            old_name='recommending_aiesec_to_a_friend',
            new_name='engagement',
        ),
        migrations.RenameField(
            model_name='nes',
            old_name='rating_explaination',
            new_name='nps_explaination',
        ),
        migrations.AddField(
            model_name='nes',
            name='nps',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='nes',
            name='team_standards',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tm.teamstandards'),
        ),
        migrations.CreateModel(
            name='PlannedVsAchieved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achieved', models.IntegerField(blank=True, default=0, null=True)),
                ('percentage', models.IntegerField(blank=True, default=0, null=True)),
                ('planned', models.ManyToManyField(blank=True, null=True, to='general.OperationalGoal')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('individual_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tm.individualplan')),
                ('team_creation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tm.teamcreation')),
                ('team_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tm.teamplan')),
            ],
        ),
        migrations.AddField(
            model_name='teamstandards',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tm.building'),
        ),
        migrations.AlterField(
            model_name='nes',
            name='percentage_of_goal_achievement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tm.plannedvsachieved'),
        ),
    ]
