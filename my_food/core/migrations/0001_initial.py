# Generated by Django 2.1.7 on 2019-12-03 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compatibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Compatibility',
                'verbose_name_plural': 'Compatibilities',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('BREAKFAST', 'Breakfast'), ('BRUNCH', 'Brunch'), ('LUNCH', 'Lunch'), ('DINNER', 'Dinner')], default='BREAKFAST', max_length=10)),
                ('calories', models.FloatField(null=True)),
                ('carbs', models.FloatField(null=True)),
                ('proteins', models.FloatField(null=True)),
                ('fat', models.FloatField(null=True)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Food',
                'verbose_name_plural': 'Food',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommend', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Recommendation',
                'verbose_name_plural': 'Recommendations',
            },
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(null=True)),
                ('amount', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Statistics',
                'verbose_name_plural': 'Statistics',
            },
        ),
        migrations.CreateModel(
            name='Wall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.IntegerField()),
                ('compatibility', models.ManyToManyField(to='core.Compatibility')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block', to='core.Food')),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block', to='core.Recommendation')),
                ('statistics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wall', to='core.Statistics')),
            ],
            options={
                'verbose_name': 'Wall',
                'verbose_name_plural': 'Walls',
            },
        ),
    ]