# Generated by Django 2.1 on 2018-09-30 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0002_auto_20180930_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FakeLeg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.IntegerField()),
                ('suburb', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('NSW', 'New South Wales'), ('VIC', 'Victoria'), ('QLD', 'Queensland'), ('TAS', 'Tasmania'), ('SA', 'South Australia'), ('WA', 'Western Australia'), ('ACT', 'Australian Capital Territory'), ('NT', 'Northern Territory')], max_length=3)),
                ('st_name', models.CharField(max_length=20, null=True)),
                ('st_number', models.IntegerField(null=True)),
                ('tenant_num', models.IntegerField()),
                ('price', models.IntegerField()),
                ('house_type', models.CharField(max_length=20, null=True)),
                ('pet', models.BooleanField(null=True)),
                ('wifi', models.BooleanField(null=True)),
                ('kitchen', models.BooleanField(null=True)),
                ('laundry', models.BooleanField(null=True)),
                ('park_lot', models.BooleanField(null=True)),
                ('brief_intro', models.CharField(max_length=500, null=True)),
                ('img_url', models.ImageField(null=True, upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('start_date', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('ID_number', models.IntegerField()),
                ('st_number', models.IntegerField()),
                ('st_name', models.CharField(max_length=20)),
                ('suburb', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('NSW', 'New South Wales'), ('VIC', 'Victoria'), ('QLD', 'Queensland'), ('TAS', 'Tasmania'), ('SA', 'South Australia'), ('WA', 'Western Australia'), ('ACT', 'Australian Capital Territory'), ('NT', 'Northern Territory')], max_length=3)),
                ('card_number', models.BigIntegerField()),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.FakeLeg')),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to='img')),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.FakeLeg')),
            ],
        ),
        migrations.AddField(
            model_name='date',
            name='PID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.FakeLeg'),
        ),
    ]
