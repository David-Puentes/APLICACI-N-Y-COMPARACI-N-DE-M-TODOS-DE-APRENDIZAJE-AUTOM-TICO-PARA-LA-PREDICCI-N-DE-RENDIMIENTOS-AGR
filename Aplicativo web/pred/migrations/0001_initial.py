# Generated by Django 2.2.2 on 2019-06-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('Variedad', models.TextField()),
                ('Clima', models.TextField(default=' ')),
                ('Fert', models.TextField(default=' ')),
                ('Suelo', models.TextField(default=' ')),
                ('Expo', models.TextField(default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('P_accu', models.DecimalField(decimal_places=2, max_digits=6)),
                ('T_avg_prev', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Rad_accu_prev1', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Desc',
            fields=[
                ('Titulo', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('Texto', models.TextField()),
            ],
        ),
    ]
