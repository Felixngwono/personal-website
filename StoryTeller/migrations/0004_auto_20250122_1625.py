# Generated by Django 3.2.16 on 2025-01-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoryTeller', '0003_blogpost_portfolioitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='events_images/')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
