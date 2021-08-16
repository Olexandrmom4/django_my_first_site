# Generated by Django 3.2.5 on 2021-08-16 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('picture1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('file', models.FileField(upload_to='files/')),
                ('tex', models.TextField()),
                ('code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='')),
                ('key_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_content', to='main.content')),
            ],
        ),
    ]
