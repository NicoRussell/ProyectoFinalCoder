# Generated by Django 3.2.9 on 2021-12-12 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=10)),
            ],
        ),
    ]
