# Generated by Django 3.0.6 on 2020-05-31 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giris', '0004_auto_20200522_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmuser',
            name='telefon',
            field=models.CharField(default=11111111111, max_length=11),
            preserve_default=False,
        ),
    ]
