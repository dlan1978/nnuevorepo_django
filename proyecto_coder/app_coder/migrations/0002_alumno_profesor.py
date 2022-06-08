# Generated by Django 4.0.4 on 2022-06-07 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('camada', models.IntegerField()),
                ('nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('legajo', models.IntegerField()),
            ],
        ),
    ]