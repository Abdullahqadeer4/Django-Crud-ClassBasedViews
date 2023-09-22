# Generated by Django 4.2.5 on 2023-09-22 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationname', models.CharField(max_length=30, unique=True)),
                ('ltype', models.CharField(max_length=50)),
                ('lserial', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=30)),
                ('itype', models.CharField(max_length=50)),
                ('iserial', models.IntegerField()),
                ('itemlocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.location')),
            ],
        ),
    ]
