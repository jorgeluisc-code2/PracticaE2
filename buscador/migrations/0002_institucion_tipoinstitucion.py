# Generated by Django 3.1.3 on 2020-11-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='tipoInstitucion',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
