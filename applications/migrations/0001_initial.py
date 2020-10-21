# Generated by Django 3.1.1 on 2020-10-21 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0013_auto_20201020_0250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('duration_id', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('product_id', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SDG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('target', models.FloatField(blank=True, default=0, null=True)),
                ('sdg_id', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_status', models.CharField(blank=True, choices=[('1', 'Sign Up'), ('2', 'Applied'), ('3', 'Accepted By Host'), ('4', 'Accepted'), ('5', 'Approved'), ('6', 'Realized'), ('7', 'Finished'), ('8', 'Complete'), ('9', 'Re-Approved'), ('10', 'Contacted'), ('11', 'Realization Broken'), ('12', 'Approval Broken'), ('13', 'Rejected'), ('14', 'Withdrawn'), ('15', 'Pending Enabler Acceptance'), ('16', 'Out Of Process')], default='Sign Up', max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sub_product_id', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_id', models.IntegerField(blank=True, default=0, null=True)),
                ('is_ir', models.BooleanField(default=False, null=True)),
                ('process_time_SU_APL', models.IntegerField(blank=True, default=0, null=True)),
                ('process_time_APL_ACC', models.IntegerField(blank=True, default=0, null=True)),
                ('process_time_APL_APD', models.IntegerField(blank=True, default=0, null=True)),
                ('process_time_SU_contacted', models.IntegerField(blank=True, default=0, null=True)),
                ('process_time_APL_contacted', models.IntegerField(blank=True, default=0, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('applied_at', models.DateTimeField(blank=True, null=True)),
                ('accepted_at', models.DateTimeField(blank=True, null=True)),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('realized_at', models.DateTimeField(blank=True, null=True)),
                ('contract_price', models.IntegerField(blank=True, default=2400, null=True)),
                ('accepted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_accepted_by', to='general.member')),
                ('application_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_manager', to='general.member')),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_approved_by', to='general.member')),
                ('contacted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_contacted_by', to='general.member')),
                ('cv_filtered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_cv_filtered_by', to='general.member')),
                ('duration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_duration', to='applications.duration')),
            ],
        ),
    ]
