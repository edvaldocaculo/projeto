# Generated by Django 4.1.1 on 2022-09-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_category_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='created_is',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='recipes',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='recipes/cover/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='title',
            field=models.CharField(max_length=63, verbose_name='titulo'),
        ),
    ]