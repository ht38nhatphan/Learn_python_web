# Generated by Django 3.2.6 on 2021-08-19 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=200)),
                ('about_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_title', models.CharField(max_length=200)),
                ('process_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('linkfb_team', models.CharField(max_length=300)),
                ('linktwitter_team', models.CharField(max_length=300)),
                ('phone_team', models.CharField(max_length=20)),
                ('image_team', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
