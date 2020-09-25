# Generated by Django 2.2.7 on 2019-11-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(default='', max_length=100)),
                ('Url', models.URLField(default='https://shaparak.ir/')),
            ],
        ),
        migrations.CreateModel(
            name='WhiteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(default='', max_length=100)),
                ('Url', models.URLField(default='https://shaparak.ir/')),
            ],
        ),
    ]