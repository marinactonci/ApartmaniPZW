# Generated by Django 3.2.12 on 2022-12-20 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_rezervacija_gost'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartman',
            name='broj_zvezdica',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
