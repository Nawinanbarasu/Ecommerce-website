# Generated by Django 5.0.1 on 2024-02-04 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Catagory',
            new_name='category',
        ),
    ]