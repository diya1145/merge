# Generated by Django 4.2.4 on 2023-10-10 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Parent'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
