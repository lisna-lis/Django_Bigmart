# Generated by Django 5.0.4 on 2024-05-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Image', models.ImageField(blank=True, null=True, upload_to='Product Image')),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
