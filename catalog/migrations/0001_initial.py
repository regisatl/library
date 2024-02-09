# Generated by Django 5.0.2 on 2024-02-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title', max_length=255)),
                ('author', models.CharField(help_text='Enter the author name', max_length=255)),
                ('summary', models.TextField(help_text='Enter a brief description of the book')),
                ('cover', models.ImageField(blank=True, upload_to='covers/')),
                ('price', models.DecimalField(decimal_places=2, help_text='Enter the price of the book', max_digits=5)),
                ('publish_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
