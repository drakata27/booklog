# Generated by Django 4.2.2 on 2023-06-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='David Goggins', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
