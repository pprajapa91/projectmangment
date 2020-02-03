# Generated by Django 3.0.2 on 2020-01-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addProject',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=100)),
                ('pname', models.CharField(max_length=100)),
                ('pdes', models.CharField(max_length=100)),
                ('cdetail', models.CharField(max_length=100)),
                ('pdeadline', models.DateField()),
                ('pstartdate', models.DateField()),
                ('pmanagedby', models.CharField(max_length=100)),
                ('pcontract', models.CharField(max_length=100)),
                ('pstatus', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Project',
            },
        ),
        migrations.CreateModel(
            name='addtask',
            fields=[
                ('Tid', models.AutoField(primary_key=True, serialize=False)),
                ('Ttitle', models.CharField(max_length=100)),
                ('Pid', models.IntegerField()),
                ('Tstatus', models.CharField(max_length=100)),
                ('Ttechnology', models.IntegerField(choices=[(1, 'Java'), (2, 'Python'), (3, 'Php'), (4, 'Wordpress'), (5, 'NodeJs')])),
                ('Tassignedto', models.CharField(max_length=100)),
                ('Tassginedby', models.CharField(max_length=100)),
                ('Tassigneddata', models.CharField(max_length=100)),
                ('Tdeadline', models.DateField()),
            ],
            options={
                'db_table': 'Task',
            },
        ),
        migrations.CreateModel(
            name='userLogin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('empid', models.IntegerField(default=1)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('is_usertype', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'login',
            },
        ),
    ]
