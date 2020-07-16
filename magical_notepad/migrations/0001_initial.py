# Generated by Django 3.0.6 on 2020-07-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('keyWord', models.CharField(help_text='Enter a Key-Word', max_length=30, primary_key=True, serialize=False)),
                ('about', models.TextField(max_length=500)),
            ],
        ),
    ]