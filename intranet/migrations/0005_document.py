# Generated by Django 5.1.5 on 2025-01-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0004_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
