# Generated by Django 3.2.9 on 2021-12-16 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRegistro', '0002_admin_suscriptor'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='fechaNacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='suscriptor',
            name='fechaNacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='fechaNacimiento',
            field=models.DateField(null=True),
        ),
    ]
