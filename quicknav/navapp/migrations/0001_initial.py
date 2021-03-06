# Generated by Django 2.2.24 on 2021-06-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('class_type', models.CharField(max_length=200)),
                ('is_admin', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NavTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('items', models.ManyToManyField(to='navapp.NavItem')),
            ],
        ),
    ]
