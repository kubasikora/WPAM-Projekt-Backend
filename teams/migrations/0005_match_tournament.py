# Generated by Django 3.1.3 on 2020-11-15 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20201115_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teams.tournament', verbose_name='Zawody'),
            preserve_default=False,
        ),
    ]