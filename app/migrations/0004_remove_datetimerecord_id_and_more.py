# Generated by Django 5.0.6 on 2024-07-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_datetimerecord_clicked_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datetimerecord',
            name='id',
        ),
        migrations.AlterField(
            model_name='datetimerecord',
            name='record_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
