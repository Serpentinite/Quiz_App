# Generated by Django 3.1.7 on 2021-05-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('quiz_content', models.TextField()),
                ('answer', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('sub_category', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'quiz',
            },
        ),
    ]