# Generated by Django 3.0.5 on 2020-07-03 12:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.date.today)),
                ('secondary_task', models.CharField(default='none', max_length=20)),
                ('episode_number', models.IntegerField(default=0)),
                ('n_distractors', models.IntegerField(default=0)),
                ('n_targets', models.IntegerField(default=0)),
                ('angle_max', models.IntegerField(default=0)),
                ('angle_min', models.IntegerField(default=0)),
                ('radius', models.IntegerField(default=0)),
                ('speed_min', models.FloatField(default=0)),
                ('speed_max', models.FloatField(default=0)),
                ('RSI', models.FloatField(default=0)),
                ('SRI_max', models.FloatField(default=0)),
                ('presentation_time', models.FloatField(default=0)),
                ('fixation_time', models.FloatField(default=0)),
                ('tracking_time', models.FloatField(default=0)),
                ('nb_target_retrieved', models.IntegerField(default=0)),
                ('nb_distract_retrieved', models.IntegerField(default=0)),
                ('id_session', models.IntegerField(default=0)),
                ('finished_session', models.BooleanField(default=False)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(default=0)),
                ('index', models.IntegerField(default=0)),
                ('wait', models.DurationField(default=datetime.timedelta(0))),
                ('tasks_csv', models.CharField(default='', max_length=200)),
                ('extra_json', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'ordering': ['study', 'day', 'index'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.CharField(max_length=100, null=True)),
                ('component', models.CharField(max_length=100, null=True)),
                ('group', models.CharField(max_length=50, null=True)),
                ('handle', models.CharField(max_length=10, null=True)),
                ('order', models.IntegerField(null=True)),
                ('prompt', models.CharField(max_length=300, null=True)),
                ('reverse', models.BooleanField(null=True)),
                ('min_val', models.IntegerField(null=1)),
                ('max_val', models.IntegerField(null=1)),
                ('step', models.IntegerField(null=1)),
                ('annotations', models.CharField(max_length=200, null=True)),
                ('widget', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=uuid.uuid4, max_length=50, unique=True)),
                ('project', models.CharField(default='', max_length=100)),
                ('base_template', models.CharField(default='base.html', max_length=50)),
                ('style', models.CharField(max_length=50, null=True)),
                ('briefing_template', models.CharField(blank=True, max_length=50, null=True)),
                ('reminder_template', models.CharField(blank=True, max_length=50, null=True)),
                ('extra_json', jsonfield.fields.JSONField(default=dict)),
                ('contact', models.EmailField(default='', max_length=254)),
            ],
            options={
                'verbose_name': 'Study',
                'verbose_name_plural': 'Studies',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, unique=True)),
                ('description', models.TextField(default='')),
                ('prompt', models.CharField(blank=True, default='', max_length=100)),
                ('view_name', models.CharField(default='', max_length=50)),
                ('info_templates_csv', models.TextField(blank=True, null=True)),
                ('extra_json', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='detection', max_length=20)),
                ('delta_orientation', models.FloatField(default=0)),
                ('success', models.BooleanField(default=False)),
                ('answer_duration', models.FloatField(default=0)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface_app.Episode')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_params', models.FloatField(default=39.116)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registration date and time')),
                ('birth_date', models.DateField(blank=True, default=datetime.date.today, help_text='day / month / year')),
                ('remind', models.BooleanField(default=True)),
                ('consent', models.BooleanField(default=False)),
                ('session_timestamp', models.DateTimeField(blank=True, null=True, verbose_name='Date-time of last finished session')),
                ('task_stack_csv', models.TextField(blank=True, default='', null=True)),
                ('extra_json', jsonfield.fields.JSONField(default=dict)),
                ('current_session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.ExperimentSession')),
                ('sessions', models.ManyToManyField(default=[], related_name='session_stack', to='interface_app.ExperimentSession')),
                ('study', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='interface_app.Study')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Participant',
                'ordering': ['birth_date'],
            },
        ),
        migrations.CreateModel(
            name='JOLD_LL_trial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('trial', models.IntegerField(null=True)),
                ('wind', models.DecimalField(decimal_places=2, max_digits=3)),
                ('init_site', models.IntegerField(null=True)),
                ('plat_site', models.IntegerField(null=True)),
                ('init_dist', models.DecimalField(decimal_places=2, max_digits=5)),
                ('end_dist', models.DecimalField(decimal_places=2, max_digits=5)),
                ('time_trial', models.DecimalField(decimal_places=1, max_digits=8)),
                ('time_block', models.DecimalField(decimal_places=1, max_digits=8)),
                ('fuel', models.IntegerField(null=True)),
                ('presses', models.IntegerField(null=True)),
                ('outcome', models.CharField(max_length=10)),
                ('interruptions', models.IntegerField(null=True)),
                ('forced', models.BooleanField(default=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface_app.ParticipantProfile')),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='interface_app.ExperimentSession')),
            ],
            options={
                'verbose_name': 'Lunar lander trial',
                'verbose_name_plural': 'Lunar lander trials',
            },
        ),
        migrations.AddField(
            model_name='experimentsession',
            name='study',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interface_app.Study', to_field='name'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(null=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface_app.ParticipantProfile')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.Question')),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.ExperimentSession')),
            ],
        ),
        migrations.AddConstraint(
            model_name='experimentsession',
            constraint=models.CheckConstraint(check=models.Q(('day__gt', 0), ('index__gt', 0), _connector='OR'), name='day_or_index_gt'),
        ),
        migrations.AlterUniqueTogether(
            name='experimentsession',
            unique_together={('study', 'day', 'index')},
        ),
    ]
