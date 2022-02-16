# Generated by Django 4.0.2 on 2022-02-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_promotion_delete_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='image',
            field=models.ImageField(upload_to='packages_files', verbose_name='Imagen'),
        ),
    ]