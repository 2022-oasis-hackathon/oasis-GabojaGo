# Generated by Django 3.2.5 on 2022-07-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_alter_scamdata_bank_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scamdata',
            name='trans_location',
        ),
        migrations.AddField(
            model_name='scamdata',
            name='h_area1',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='scamdata',
            name='h_area2',
            field=models.IntegerField(default=1),
        ),
    ]
