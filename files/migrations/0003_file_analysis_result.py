# Generated by Django 5.1.3 on 2024-11-20 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_file_transcription_alter_file_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='analysis_result',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
