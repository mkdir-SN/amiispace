# Generated by Django 3.0.7 on 2020-06-22 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amiispace_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycard',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amiispace_app.Card'),
        ),
    ]
