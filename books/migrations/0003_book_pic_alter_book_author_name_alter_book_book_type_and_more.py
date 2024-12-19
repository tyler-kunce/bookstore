# Generated by Django 4.2.16 on 2024-11-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('hc', 'Hard cover'), ('eb', 'E-Book'), ('ab', 'Audiobook')], default='hc', max_length=12),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('cl', 'Classic'), ('ro', 'Romantic'), ('co', 'Comic'), ('fa', 'Fantasy'), ('ho', 'Horror'), ('ed', 'Educational')], default='cl', max_length=12),
        ),
    ]