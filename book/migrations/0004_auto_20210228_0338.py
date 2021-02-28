# Generated by Django 3.1.7 on 2021-02-28 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20210227_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.member'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='checked_out_to',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checkedout_books', to='book.member'),
        ),
        migrations.AlterField(
            model_name='book',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='books_liked', to='book.Member'),
        ),
    ]