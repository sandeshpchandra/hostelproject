# Generated by Django 4.2.7 on 2024-03-18 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signupdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('sdep', models.CharField(blank=True, max_length=50, null=True)),
                ('sroom', models.CharField(blank=True, max_length=50, null=True)),
                ('semail', models.CharField(blank=True, max_length=50, null=True)),
                ('pass1', models.CharField(blank=True, max_length=50, null=True)),
                ('pass2', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
