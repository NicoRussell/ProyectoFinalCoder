# Generated by Django 3.2.9 on 2021-12-16 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRegistro', '0003_auto_20211216_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='suscriptor',
            name='email',
            field=models.EmailField(default=' ', max_length=254),
            preserve_default=False,
        ),
    ]
