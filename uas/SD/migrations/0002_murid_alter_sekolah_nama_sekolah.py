# Generated by Django 4.1.1 on 2023-01-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='murid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sekolah', models.CharField(max_length=50)),
                ('NPSN', models.CharField(max_length=50)),
                ('Jmlhmurid', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='sekolah',
            name='nama_sekolah',
            field=models.CharField(max_length=50),
        ),
    ]
