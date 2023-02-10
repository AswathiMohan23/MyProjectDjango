# Generated by Django 4.1.6 on 2023-02-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=30, verbose_name='company_name')),
                ('company_location', models.CharField(blank=True, max_length=30, verbose_name='company_location')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='employee_name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='place',
            field=models.CharField(blank=True, max_length=200, verbose_name='place'),
        ),
    ]
