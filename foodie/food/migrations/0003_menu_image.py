# Generated by Django 4.1.3 on 2022-12-19 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0002_bookings_menu"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="image",
            field=models.ImageField(default="image.jpeg", upload_to="images/"),
            preserve_default=False,
        ),
    ]