# Generated by Django 4.0.5 on 2022-06-21 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.generators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.CharField(default=utils.generators.generateID, max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('picture', models.ImageField(blank=True, upload_to=utils.generators.generateNameFile)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isOrganizer', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.community')),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(through='communities.Member', to=settings.AUTH_USER_MODEL),
        ),
    ]
