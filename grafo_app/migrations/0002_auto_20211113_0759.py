# Generated by Django 3.2.8 on 2021-11-13 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grafo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.AlterModelOptions(
            name='tejido',
            options={'verbose_name': 'Tejido', 'verbose_name_plural': 'Tejidos'},
        ),
        migrations.AlterField(
            model_name='tejido',
            name='color',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tejido',
            name='inflammation',
            field=models.FloatField(verbose_name='Inflamación'),
        ),
        migrations.AlterField(
            model_name='tejido',
            name='temperatura',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='tejido',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grafo_app.paciente'),
        ),
    ]