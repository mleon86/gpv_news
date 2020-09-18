# Generated by Django 3.1.1 on 2020-09-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='post_image')),
                ('video_leccion', models.CharField(max_length=150)),
                ('create_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Leccion',
                'verbose_name_plural': 'Lecciones',
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('comentario', models.CharField(max_length=200)),
                ('video_invitacion', models.CharField(max_length=150)),
                ('create_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('lecciones', models.ManyToManyField(to='recursos.Leccion')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['create_at'],
            },
        ),
    ]