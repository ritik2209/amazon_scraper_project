# Generated by Django 4.2 on 2023-04-16 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('is_sponsored', models.BooleanField()),
                ('search_date', models.DateField()),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.keyword')),
            ],
            options={
                'ordering': ('search_date',),
            },
        ),
    ]
