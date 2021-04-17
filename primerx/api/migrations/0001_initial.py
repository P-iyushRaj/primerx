# Generated by Django 3.2 on 2021-04-17 13:00

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='primerx_field_model',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('prime_form_id', models.IntegerField(blank=True, null=True)),
                ('prime_patient_id', models.IntegerField(blank=True, null=True)),
                ('prime_address_id', models.IntegerField(blank=True, null=True)),
                ('prime_first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('prime_lst_name', models.CharField(blank=True, max_length=200, null=True)),
                ('prime_middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('prime_suffix_form', models.CharField(blank=True, max_length=200, null=True)),
                ('prime_prefix_form', models.CharField(blank=True, max_length=200, null=True)),
                ('prime_work_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('prime_Social_security_num', models.IntegerField(blank=True, null=True)),
                ('prime_education', models.CharField(blank=True, max_length=200, null=True)),
                ('prime_address_street', models.CharField(blank=True, max_length=200, null=True)),
                ('prime_address_city', models.CharField(blank=True, max_length=200, null=True)),
                ('prime_address_state', models.CharField(blank=True, max_length=200, null=True)),
                ('prime_emergency_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('prime_emergency_name', models.CharField(blank=True, max_length=200, null=True)),
                ('prime_emergency_relation', models.CharField(blank=True, max_length=200, null=True)),
                ('prime_sex', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]