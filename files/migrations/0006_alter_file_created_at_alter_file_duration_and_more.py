# Generated by Django 5.1.3 on 2024-11-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_alter_file_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='file',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Длительность'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='uploads/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='file',
            name='language',
            field=models.CharField(max_length=50, verbose_name='Выбор языка'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя файла'),
        ),
        migrations.AlterField(
            model_name='file',
            name='speakers',
            field=models.IntegerField(verbose_name='Спикеры'),
        ),
        migrations.AlterField(
            model_name='file',
            name='status',
            field=models.CharField(choices=[('processing', 'В процессе'), ('completed', 'Обработан'), ('error', 'Ошибка')], default='processing', max_length=50, verbose_name='Статус'),
        ),
    ]