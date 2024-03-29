# Generated by Django 4.2.2 on 2024-03-24 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citation', '0005_rename_nunber_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='literary_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isbn_no', models.CharField(max_length=25)),
                ('author_name', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('publish_year', models.CharField(max_length=255)),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citation.language')),
            ],
        ),
    ]
