# Generated by Django 2.2 on 2019-04-04 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('ENG', 'ENGLISH'), ('HIN', 'Hindi')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('word', models.CharField(max_length=100)),
                ('pos', models.CharField(choices=[('NNP', 'NNP'), ('VB', 'VB')], max_length=10)),
                ('chunk', models.CharField(choices=[('B-NP', 'B-NP'), ('B-VP', 'B-VP')], max_length=10)),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chunking.Sentence')),
            ],
        ),
    ]
