# Generated by Django 4.0.8 on 2022-11-11 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbAplication',
            fields=[
                ('id_Aplication', models.AutoField(db_column='id_Aplication', primary_key=True, serialize=False)),
                ('nameAplication', models.CharField(db_column='nameAplication', max_length=255)),
                ('sectionAplication', models.CharField(db_column='sectionAplication', max_length=255)),
            ],
            options={
                'db_table': 'Tb_Aplication',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbCity',
            fields=[
                ('id_City', models.AutoField(db_column='id_City', primary_key=True, serialize=False)),
                ('nameCity', models.CharField(db_column='nameCity', max_length=255)),
            ],
            options={
                'db_table': 'Tb_City',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbCountry',
            fields=[
                ('id_Country', models.AutoField(db_column='id_Country', primary_key=True, serialize=False)),
                ('nameCountry', models.CharField(db_column='nameCountry', max_length=255)),
            ],
            options={
                'db_table': 'Tb_Country',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbDevice',
            fields=[
                ('id_Device', models.AutoField(db_column='id_Device', primary_key=True, serialize=False)),
                ('nameDevice', models.CharField(db_column='nameDevice', max_length=255)),
                ('tokenDevice', models.CharField(db_column='tokenDevice', max_length=255)),
                ('creationDateDevice', models.DateTimeField(db_column='creationDateDevice', null=True)),
            ],
            options={
                'db_table': 'Tb_Device',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbDeviceType',
            fields=[
                ('id_DeviceType', models.AutoField(db_column='id_DeviceType', primary_key=True, serialize=False)),
                ('nameDeviceType', models.CharField(db_column='nameDeviceType', max_length=255)),
            ],
            options={
                'db_table': 'Tb_DeviceType',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbHwPlatform',
            fields=[
                ('id_HwPlatform', models.AutoField(db_column='id_HwPlatform', primary_key=True, serialize=False)),
                ('nameHwPlatform', models.CharField(db_column='nameHwPlatform', max_length=255)),
            ],
            options={
                'db_table': 'Tb_HwPlatform',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbOrganization',
            fields=[
                ('id_Organization', models.AutoField(db_column='id_Organization', primary_key=True, serialize=False)),
                ('nameOrganization', models.CharField(db_column='nameOrganization', max_length=255)),
                ('taxIdOrganization', models.CharField(db_column='taxIdOrganization', max_length=255)),
                ('addressOrganization', models.CharField(db_column='addressOrganization', max_length=255)),
                ('contactEmailOrganization', models.CharField(db_column='contactEmailOrganization', max_length=255)),
                ('isActive', models.BooleanField(db_column='isActive', default=True)),
                ('id_City', models.ForeignKey(db_column='id_City', on_delete=django.db.models.deletion.PROTECT, to='organization.tbcity')),
                ('id_Country', models.ForeignKey(db_column='id_Country', on_delete=django.db.models.deletion.PROTECT, to='organization.tbcountry')),
            ],
            options={
                'db_table': 'Tb_Organization',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbOs',
            fields=[
                ('id_Os', models.AutoField(db_column='Id_Os', primary_key=True, serialize=False)),
                ('nameOs', models.CharField(db_column='nameOs', max_length=255)),
            ],
            options={
                'db_table': 'Tb_Os',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbSettingsType',
            fields=[
                ('id_SettingsType', models.AutoField(db_column='id_SettingsType', primary_key=True, serialize=False)),
                ('nameSettingsType', models.CharField(db_column='nameSettingsType', max_length=255)),
            ],
            options={
                'db_table': 'Tb_SettingsType',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbSite',
            fields=[
                ('id_Site', models.AutoField(db_column='id_Site', primary_key=True, serialize=False)),
                ('nameSite', models.CharField(db_column='nameSite', max_length=255)),
                ('addressSite', models.CharField(db_column='addressSite', max_length=255)),
                ('isActive', models.BooleanField(db_column='isActive', default=True)),
                ('id_City', models.ForeignKey(db_column='id_City', on_delete=django.db.models.deletion.PROTECT, to='organization.tbcity')),
                ('id_Country', models.ForeignKey(db_column='id_Country', on_delete=django.db.models.deletion.PROTECT, to='organization.tbcountry')),
                ('id_Organization', models.ForeignKey(db_column='id_Organization', on_delete=django.db.models.deletion.PROTECT, to='organization.tborganization')),
            ],
            options={
                'db_table': 'Tb_Site',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbTokenType',
            fields=[
                ('id_TokenType', models.AutoField(db_column='id_TokenType', primary_key=True, serialize=False)),
                ('nameTokenType', models.CharField(db_column='nameTokenType', max_length=255)),
            ],
            options={
                'db_table': 'Tb_TokenType',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbZone',
            fields=[
                ('id_Zone', models.AutoField(db_column='id_Zone', primary_key=True, serialize=False)),
                ('nameZone', models.CharField(db_column='nameZone', max_length=255)),
                ('id_Site', models.ForeignKey(db_column='id_Site', on_delete=django.db.models.deletion.PROTECT, to='organization.tbsite')),
            ],
            options={
                'db_table': 'Tb_Zone',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbToken',
            fields=[
                ('id_Token', models.AutoField(db_column='id_Token', primary_key=True, serialize=False)),
                ('valueToken', models.CharField(db_column='valueToken', max_length=255)),
                ('id_Owner', models.IntegerField(db_column='id_Owner')),
                ('id_TokenType', models.ForeignKey(db_column='id_TokenType', on_delete=django.db.models.deletion.PROTECT, to='organization.tbtokentype')),
            ],
            options={
                'db_table': 'Tb_Token',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbSettings',
            fields=[
                ('id_Settings', models.AutoField(db_column='id_Setting', primary_key=True, serialize=False)),
                ('id_Owner', models.IntegerField(db_column='id_Owner')),
                ('valueSettings', models.CharField(db_column='valueSettings', max_length=255)),
                ('id_SettingsType', models.ForeignKey(db_column='id_SettingsType', on_delete=django.db.models.deletion.PROTECT, to='organization.tbsettingstype')),
            ],
            options={
                'db_table': 'Tb_Settings',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbPeople',
            fields=[
                ('id_People', models.AutoField(db_column='id_People', primary_key=True, serialize=False)),
                ('namePeople', models.CharField(db_column='namePeople', max_length=255)),
                ('emailPeople', models.CharField(db_column='emailPeople', max_length=255)),
                ('phonePeople', models.IntegerField(db_column='phonePeople')),
                ('id_Organization', models.ForeignKey(db_column='id_Organization', on_delete=django.db.models.deletion.PROTECT, to='organization.tborganization')),
            ],
            options={
                'db_table': 'Tb_People',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TbLocalization',
            fields=[
                ('id_Localization', models.AutoField(db_column='id_Localization', primary_key=True, serialize=False)),
                ('gpsDataLocation', models.CharField(db_column='gpsDataLocation', max_length=255)),
                ('isActive', models.BooleanField(db_column='isActive', default=True)),
                ('idZone', models.ForeignKey(db_column='id_Zone', on_delete=django.db.models.deletion.PROTECT, to='organization.tbzone')),
                ('id_Device', models.ForeignKey(db_column='id_Device', on_delete=django.db.models.deletion.PROTECT, to='organization.tbdevice')),
            ],
            options={
                'db_table': 'Tb_Localization',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='tbdevice',
            name='id_DeviceType',
            field=models.ForeignKey(db_column='id_DeviceType', on_delete=django.db.models.deletion.PROTECT, to='organization.tbdevicetype'),
        ),
        migrations.AddField(
            model_name='tbdevice',
            name='id_Organization',
            field=models.ForeignKey(db_column='id_Organization', on_delete=django.db.models.deletion.PROTECT, to='organization.tborganization'),
        ),
        migrations.AddField(
            model_name='tbdevice',
            name='id_Os',
            field=models.ForeignKey(db_column='id_Os', on_delete=django.db.models.deletion.PROTECT, to='organization.tbos'),
        ),
        migrations.AddField(
            model_name='tbdevice',
            name='id_hwPlatform',
            field=models.ForeignKey(db_column='id_HwPlatform', on_delete=django.db.models.deletion.PROTECT, to='organization.tbhwplatform'),
        ),
        migrations.AddField(
            model_name='tbcity',
            name='id_Country',
            field=models.ForeignKey(db_column='id_Country', on_delete=django.db.models.deletion.PROTECT, to='organization.tbcountry'),
        ),
        migrations.CreateModel(
            name='TbAutorization',
            fields=[
                ('id_Autorization', models.AutoField(db_column='id_Autorization', primary_key=True, serialize=False)),
                ('sectionAutorization', models.CharField(db_column='sectionAutorization', max_length=255)),
                ('id_Aplication', models.ForeignKey(db_column='id_Aplication', on_delete=django.db.models.deletion.PROTECT, to='organization.tbaplication')),
                ('id_Device', models.ForeignKey(db_column='id_Device', on_delete=django.db.models.deletion.PROTECT, to='organization.tbdevice')),
                ('id_People', models.ForeignKey(db_column='id_People', on_delete=django.db.models.deletion.PROTECT, to='organization.tbpeople')),
            ],
            options={
                'db_table': 'Tb_Autorization',
                'managed': True,
            },
        ),
    ]
