# Generated by Django 4.2.2 on 2024-03-16 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citation', '0002_alter_sindhi_accession_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malayalam',
            name='year_of_dc',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='malayalam',
            name='year_pub',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='northeast',
            name='accession_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='northeast',
            name='year',
            field=models.CharField(max_length=255),
        ),
    ]
