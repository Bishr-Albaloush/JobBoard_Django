# Generated by Django 4.1.3 on 2022-11-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_tybe', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='jop',
        ),
    ]