# Generated by Django 2.0.2 on 2019-12-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0007_auto_20191205_1309'),
        ('xsauth', '0002_user_collect'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='read',
            field=models.ManyToManyField(related_name='readers', related_query_name='readers', to='novel.Novel'),
        ),
    ]
