# Generated by Django 4.0.3 on 2022-04-21 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyLicense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=3)),
                ('Father_Name', models.CharField(max_length=100)),
                ('Scc_Number', models.CharField(max_length=11)),
                ('Adhar_Number', models.CharField(max_length=12)),
            ],
        ),
    ]
