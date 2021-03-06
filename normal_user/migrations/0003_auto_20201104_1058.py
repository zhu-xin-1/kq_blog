# Generated by Django 3.1.2 on 2020-11-04 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0002_auto_20201031_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sudent_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teach', models.CharField(max_length=4)),
                ('students_number', models.SmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='authority',
            name='authorit_add',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='authority',
            name='authorit_delete',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='authority',
            name='authorit_query',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='authority',
            name='authorit_update',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='authority',
            name='authority_degree',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Student_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
                ('age', models.SmallIntegerField()),
                ('height', models.SmallIntegerField()),
                ('weigth', models.SmallIntegerField()),
                ('class_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='normal_user.sudent_class')),
            ],
        ),
        migrations.AddField(
            model_name='normal_user',
            name='user_sudent_id',
            field=models.ManyToManyField(blank=True, null=True, to='normal_user.Student_detail'),
        ),
    ]
