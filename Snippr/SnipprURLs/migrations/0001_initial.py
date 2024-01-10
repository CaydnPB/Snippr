# Generated by Django 4.2.8 on 2024-01-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnipprSnippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('code', models.TextField()),
            ],
            options={
                'verbose_name': 'Snippr Snippet',
                'verbose_name_plural': 'Snippr Snippets',
            },
        ),
    ]
