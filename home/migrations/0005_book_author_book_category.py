# Generated by Django 5.0.6 on 2024-06-26 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.category'),
            preserve_default=False,
        ),
    ]
