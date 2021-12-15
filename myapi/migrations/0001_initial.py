# Generated by Django 3.2.6 on 2021-12-15 19:57

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/', verbose_name='Image')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Job Title', max_length=200)),
                ('description', models.TextField(help_text='Job Description')),
                ('company', models.CharField(help_text='Company Name', max_length=200)),
                ('location', models.CharField(help_text='Location', max_length=200)),
                ('link', models.URLField(help_text='Link to Job')),
                ('date', models.DateField(help_text='Publish Date')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='images/')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]
