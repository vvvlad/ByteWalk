# Generated by Django 3.0.8 on 2020-08-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
