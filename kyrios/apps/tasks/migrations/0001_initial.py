# Generated by Django 4.0.5 on 2022-06-17 14:46

from django.db import migrations, models
import django.db.models.deletion
import utils.generators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.CharField(default=utils.generators.generateID, max_length=12, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('delivery_to', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.community')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=utils.generators.generateNameFile)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
