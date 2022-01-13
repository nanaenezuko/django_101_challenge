# Generated by Django 4.0.1 on 2022-01-11 03:15

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photouploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postphoto',
            name='caption',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postphoto',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=''),
        ),
    ]