# Generated by Django 5.1 on 2024-08-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news_post',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news_post',
            name='author_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Автор новости'),
        ),
    ]
