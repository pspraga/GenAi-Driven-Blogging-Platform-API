# Generated by Django 5.1.4 on 2024-12-22 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': [('can_view_article', 'Can view articles'), ('can_edit_article', 'Can edit articles'), ('can_delete_article', 'Can delete articles')]},
        ),
    ]