# Generated by Django 2.0.4 on 2018-04-26 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_type', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'client_types',
            },
        ),
        migrations.CreateModel(
            name='ConversionChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_correct', models.PositiveSmallIntegerField()),
                ('score', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'conversion_charts',
            },
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_spent', models.PositiveSmallIntegerField(help_text='Mark down time spent in minutes. <em>Example: for 2 minutes 30 seconds mark down 2.5.</em>')),
                ('notes', models.TextField(max_length=1000)),
            ],
            options={
                'db_table': 'observations',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(help_text='Please use the following format: <em>555-555-5555</em>', max_length=16)),
                ('address1', models.CharField(max_length=150)),
                ('address2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.PositiveIntegerField(blank=True, null=True)),
                ('enrollment_status', models.CharField(max_length=25)),
                ('payment_status', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('hours_purchased', models.PositiveSmallIntegerField(default=0)),
                ('hours_received', models.PositiveSmallIntegerField(default=0)),
                ('payrate', models.PositiveSmallIntegerField(default=0)),
                ('focus_area', models.CharField(max_length=50)),
                ('sat_diagnostic', models.PositiveIntegerField(blank=True, null=True)),
                ('sat_diagnostic_reading_and_writing', models.PositiveIntegerField(blank=True, null=True)),
                ('sat_diagnostic_math', models.PositiveIntegerField(blank=True, null=True)),
                ('sat_best_practice', models.PositiveIntegerField(blank=True, null=True)),
                ('sat_best_practice_reading_and_writing', models.PositiveIntegerField(blank=True, null=True)),
                ('sat_best_practice_math', models.PositiveIntegerField(blank=True, null=True)),
                ('sat_best_official', models.PositiveIntegerField(blank=True, null=True)),
                ('sat_best_official_reading_and_writing', models.PositiveIntegerField(blank=True, null=True)),
                ('sat_best_official_math', models.PositiveIntegerField(blank=True, null=True)),
                ('sat_best_official_essay', models.PositiveIntegerField(blank=True, null=True)),
                ('lsat_diagnostic', models.PositiveIntegerField(blank=True, null=True)),
                ('lsat_best_practice', models.PositiveIntegerField(blank=True, null=True)),
                ('lsat_best_official', models.PositiveIntegerField(blank=True, null=True)),
                ('act_diagnostic', models.PositiveIntegerField(blank=True, null=True)),
                ('act_best_practice', models.PositiveIntegerField(blank=True, null=True)),
                ('act_best_official', models.PositiveIntegerField(blank=True, null=True)),
                ('college_matriculated', models.CharField(max_length=150)),
                ('colleges_accepted', models.CharField(max_length=250)),
                ('scholarship_money', models.CharField(max_length=150)),
                ('law_school_matriculated', models.CharField(max_length=150)),
                ('law_schools_accepted', models.CharField(max_length=250)),
                ('client_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.ClientType')),
            ],
            options={
                'db_table': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.PositiveIntegerField()),
                ('correct_answer', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_code', models.CharField(max_length=10)),
                ('type_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'question_types',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_answer', models.CharField(max_length=50)),
                ('time_spent', models.PositiveSmallIntegerField(help_text='Mark down time spent in minutes. <em>Example: for 2 minutes 30 seconds mark down 2.5.</em>')),
                ('guess', models.NullBooleanField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Question')),
            ],
            options={
                'db_table': 'results',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sections',
            },
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsection_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'subsections',
            },
        ),
        migrations.CreateModel(
            name='Subsubsection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsubsection_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'subsubsections',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tests',
            },
        ),
        migrations.AddField(
            model_name='result',
            name='section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Section'),
        ),
        migrations.AddField(
            model_name='result',
            name='test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Test'),
        ),
        migrations.AddField(
            model_name='result',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.QuestionType'),
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Section'),
        ),
        migrations.AddField(
            model_name='question',
            name='subsection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Subsection'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Test'),
        ),
        migrations.AddField(
            model_name='observation',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Question'),
        ),
        migrations.AddField(
            model_name='observation',
            name='section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Section'),
        ),
        migrations.AddField(
            model_name='observation',
            name='subsection_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Subsection'),
        ),
        migrations.AddField(
            model_name='observation',
            name='subsubsection_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Subsubsection'),
        ),
        migrations.AddField(
            model_name='observation',
            name='test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Test'),
        ),
        migrations.AddField(
            model_name='observation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversionchart',
            name='section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Section'),
        ),
        migrations.AddField(
            model_name='conversionchart',
            name='test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Test'),
        ),
    ]