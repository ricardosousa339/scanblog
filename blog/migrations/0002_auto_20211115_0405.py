# Generated by Django 3.2.9 on 2021-11-15 04:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='resumo',
        ),
        migrations.AddField(
            model_name='post',
            name='summary',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
