# Generated by Django 3.2.12 on 2022-02-06 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0004_alter_branch_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('account_num', models.CharField(max_length=128, unique=True)),
                ('balance', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Customer',
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
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='AccountOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bank_app.account')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bank_app.customer')),
            ],
            options={
                'db_table': 'account_owners',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='account_holders',
            field=models.ManyToManyField(through='bank_app.AccountOwner', to='bank_app.Customer'),
        ),
    ]
