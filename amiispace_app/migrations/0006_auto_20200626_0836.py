# Generated by Django 3.0.7 on 2020-06-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amiispace_app', '0005_auto_20200626_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycard',
            name='quality',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], default='New', max_length=5),
        ),
    ]