# Generated by Django 4.2.5 on 2023-11-12 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('course_categories',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='course_name',
            new_name='course_categories',
        ),
    ]
