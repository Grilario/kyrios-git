# Generated by Django 4.0.5 on 2022-06-30 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachment',
            old_name='task',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='content',
        ),
        migrations.AddField(
            model_name='message',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='description',
            field=models.CharField(default=1, max_length=500, verbose_name='Descrição'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]
