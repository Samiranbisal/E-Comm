# Generated by Django 5.1.1 on 2024-10-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('category', models.CharField(choices=[('CR', 'Cure'), ('ML', 'Milk'), ('EG', 'Egg'), ('FR', 'Fruit'), ('VE', 'Vegetable'), ('GH', 'Ghee'), ('FL', 'Flour'), ('SP', 'Spice'), ('IC', 'Ice-Creams')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]