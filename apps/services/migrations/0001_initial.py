# Generated by Django 2.2.2 on 2019-08-02 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('important', models.BooleanField(default=False)),
                ('text', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.TextField(max_length=50, unique=True)),
                ('status', models.CharField(choices=[('online', 'online'), ('offline', 'offline')], default='online', max_length=10)),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.ServiceMessage')),
            ],
        ),
    ]
