# Generated by Django 2.2.dev20180610131139 on 2018-06-19 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=30)),
                ('passwd', models.CharField(max_length=1024)),
                ('rtime', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'accounts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('cardid', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=512)),
                ('ptime', models.DateTimeField()),
            ],
            options={
                'db_table': 'cards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Upinfo',
            fields=[
                ('upid', models.IntegerField(primary_key=True, serialize=False)),
                ('upname', models.CharField(max_length=64)),
                ('des', models.CharField(blank=True, max_length=512, null=True)),
                ('wtime', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'upinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('wid', models.AutoField(primary_key=True, serialize=False)),
                ('uwtime', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'watch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usrinfo',
            fields=[
                ('uid', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='watch.Accounts')),
                ('des', models.CharField(blank=True, max_length=512, null=True)),
                ('face', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'usrinfo',
                'managed': False,
            },
        ),
    ]
