# Generated by Django 3.0.7 on 2020-06-26 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('amiispace_app', '0003_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycard',
            name='card',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='amiispace_app.Card'),
        ),
        migrations.AlterField(
            model_name='mycard',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mycard',
            name='quality',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], default='New', max_length=5),
        ),
    ]
