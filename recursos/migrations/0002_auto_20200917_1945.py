# Generated by Django 3.1.1 on 2020-09-17 19:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leccion',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]