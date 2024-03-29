# Generated by Django 3.1.1 on 2020-10-21 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0014_auto_20201021_2230'),
        ('applications', '0001_initial'),
        ('opportunities', '0006_auto_20201021_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='EP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_sign_up', models.DateTimeField(blank=True, null=True)),
                ('applications_count', models.IntegerField(default=0, null=True)),
                ('contacted_at', models.DateTimeField(blank=True, null=True)),
                ('applications', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ep_applications', to='applications.application')),
                ('contacted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ep_contacted_by', to='general.member')),
                ('managers', models.ManyToManyField(related_name='ep_managers', to='general.Member')),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ep_member', to='general.member')),
                ('opportunities_applied_to', models.ManyToManyField(related_name='ep_opportunities', to='opportunities.Opportunity')),
                ('selected_program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='applications.product')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ep_status', to='applications.status')),
            ],
        ),
    ]
