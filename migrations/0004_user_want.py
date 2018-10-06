# Generated by Django 2.1 on 2018-09-30 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NearBeach', '0003_auto_20180923_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_want',
            fields=[
                ('user_want_id', models.AutoField(primary_key=True, serialize=False)),
                ('want_choice', models.CharField(choices=[('0', 'Do not want to do'), ('1', 'Want to do')], max_length=50)),
                ('want_choice_text', models.CharField(max_length=50)),
                ('want_skill', models.CharField(choices=[('0', 'Can not do'), ('1', 'Willing to learn'), ('2', 'Knows a little'), ('3', 'Knows a lot'), ('4', 'Proficient')], max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_want_change_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_want',
            },
        ),
    ]