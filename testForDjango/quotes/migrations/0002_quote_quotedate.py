# Generated by Django 2.1.3 on 2018-11-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='quotedate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
