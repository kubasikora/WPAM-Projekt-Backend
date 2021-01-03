# Generated by Django 3.1.3 on 2021-01-03 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20201122_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='teams.country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='sport',
            field=models.CharField(choices=[('FOOTBALL', 'Piłka nożna'), ('VOLLEYBALL', 'Siatkówka'), ('TENNIS', 'Tenis')], default='FOOTBALL', max_length=15, verbose_name='Sport'),
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(max_length=4, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='match',
            name='dateOfStart',
            field=models.DateTimeField(verbose_name='Time of start'),
        ),
        migrations.AlterField(
            model_name='match',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='Is finished'),
        ),
        migrations.AlterField(
            model_name='match',
            name='outcome',
            field=models.CharField(choices=[('N', 'N'), ('1', '1'), ('2', '2'), ('X', 'X')], default='N', max_length=1, verbose_name='Result'),
        ),
        migrations.AlterField(
            model_name='match',
            name='playerOne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playerOnes', to='teams.contestant', verbose_name='Contestant 1'),
        ),
        migrations.AlterField(
            model_name='match',
            name='playerOneResult',
            field=models.PositiveIntegerField(default=0, verbose_name='Score 1'),
        ),
        migrations.AlterField(
            model_name='match',
            name='playerTwo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playerTwos', to='teams.contestant', verbose_name='Contestant 2'),
        ),
        migrations.AlterField(
            model_name='match',
            name='playerTwoResult',
            field=models.PositiveIntegerField(default=0, verbose_name='Score 2'),
        ),
        migrations.AlterField(
            model_name='match',
            name='sport',
            field=models.CharField(choices=[('FOOTBALL', 'Piłka nożna'), ('VOLLEYBALL', 'Siatkówka'), ('TENNIS', 'Tenis')], default='FOOTBALL', max_length=15, verbose_name='Sport'),
        ),
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.tournament', verbose_name='Tournament'),
        ),
        migrations.AlterField(
            model_name='match',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.venue', verbose_name='Venue'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='contestants',
            field=models.ManyToManyField(blank=True, to='teams.Contestant', verbose_name='Contestants'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='dateOfStart',
            field=models.DateTimeField(verbose_name='Time of start'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='domestic',
            field=models.BooleanField(default=True, verbose_name='Is domestic league'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='Is finished'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='sport',
            field=models.CharField(choices=[('FOOTBALL', 'Piłka nożna'), ('VOLLEYBALL', 'Siatkówka'), ('TENNIS', 'Tenis')], default='FOOTBALL', max_length=15, verbose_name='Sport'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='city',
            field=models.CharField(max_length=25, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='latitude',
            field=models.FloatField(max_length=10, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='longitude',
            field=models.FloatField(max_length=10, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
