# Generated by Django 3.1.3 on 2020-11-22 14:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20201116_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venue',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='tournament',
            name='dateOfStart',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Czas rozpoczęcia'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
