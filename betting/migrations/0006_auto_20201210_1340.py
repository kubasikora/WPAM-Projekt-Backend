# Generated by Django 3.1.3 on 2020-12-10 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0005_auto_20201210_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='user',
        ),
        migrations.AddField(
            model_name='bet',
            name='participant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='betting.participant', verbose_name='Członek ligi'),
            preserve_default=False,
        ),
    ]
