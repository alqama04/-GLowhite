# Generated by Django 4.0.3 on 2022-03-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_title', models.CharField(blank=True, max_length=255, null=True)),
                ('carousel_description', models.TextField(blank=True, null=True)),
                ('carousel_image', models.ImageField(upload_to='photos/carouselImage')),
            ],
            options={
                'verbose_name_plural': 'Sliders',
            },
        ),
    ]