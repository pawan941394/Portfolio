# Generated by Django 4.0.6 on 2022-07-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliowork', '0005_abousus_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_Image', models.ImageField(upload_to='skills')),
            ],
        ),
    ]
