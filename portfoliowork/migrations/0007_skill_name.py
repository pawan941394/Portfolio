# Generated by Django 4.0.6 on 2022-07-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliowork', '0006_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
