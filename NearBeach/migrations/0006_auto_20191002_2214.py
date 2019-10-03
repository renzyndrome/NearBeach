# Generated by Django 2.1.7 on 2019-10-02 22:14

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0005_requirement_customer_requirement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='campus_fax',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=20, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='campus',
            name='campus_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=20, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='customer_campus',
            name='customer_fax',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None),
        ),
        migrations.AlterField(
            model_name='customer_campus',
            name='customer_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None),
        ),
    ]
