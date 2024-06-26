# Generated by Django 4.2.3 on 2024-04-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Start', '0006_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hero_images')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Hero Section',
            },
        ),
    ]
