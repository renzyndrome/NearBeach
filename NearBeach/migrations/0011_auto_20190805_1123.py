# Generated by Django 2.1.7 on 2019-08-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0010_auto_20190801_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement_item',
            name='task_story_point_max',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='requirement_item',
            name='task_story_point_min',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='nearbeach_option',
            name='story_point_hour_max',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='nearbeach_option',
            name='story_point_hour_min',
            field=models.IntegerField(default=4),
        ),
    ]
