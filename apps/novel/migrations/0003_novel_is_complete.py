# Generated by Django 2.0.2 on 2019-12-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0002_auto_20191204_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
