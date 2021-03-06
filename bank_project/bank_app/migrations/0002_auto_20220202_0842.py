# Generated by Django 3.2.12 on 2022-02-02 08:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('passport_num', models.CharField(max_length=128, unique=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('city', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.AddField(
            model_name='branch',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='branch',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='BranchEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=128)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bank_app.branch')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bank_app.employee')),
            ],
            options={
                'db_table': 'branch_employees',
            },
        ),
    ]
