# Generated by Django 3.2.1 on 2021-05-06 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CerealCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CerealImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=9999)),
                ('cereal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cereal.cereal')),
            ],
        ),
        migrations.AddField(
            model_name='cereal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cereal.cerealcategory'),
        ),
    ]
