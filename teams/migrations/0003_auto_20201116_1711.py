# Generated by Django 3.1.3 on 2020-11-16 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20201116_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('match_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teams.match')),
            ],
            bases=('teams.match',),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa obiektu')),
                ('city', models.CharField(max_length=25, verbose_name='Miasto')),
                ('longitude', models.FloatField(max_length=10, verbose_name='Długość geograficzna')),
                ('latitude', models.FloatField(max_length=10, verbose_name='Wysokość geograficzna')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.country', verbose_name='Kraj')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.venue', verbose_name='Obiekt'),
        ),
    ]
