from django.db import models

#  -- General Tables -- #
class TbCity(models.Model):
    id_City    = models.AutoField(db_column='id_City', primary_key=True)
    nameCity   = models.CharField(db_column='nameCity' , max_length=255 , null=False)
    id_Country = models.ForeignKey('TbCountry', db_column='id_Country' , on_delete=models.PROTECT)

    def __str__(self):
        return self.nameCity
    class Meta:
        managed  = True
        db_table = 'Tb_City'

class TbCountry(models.Model):
    id_Country  = models.AutoField(db_column='id_Country', primary_key=True)
    nameCountry = models.CharField(db_column='nameCountry',  max_length=255 , null=False)

    def __str__(self):
        return self.nameCountry
    class Meta:
        managed  = True
        db_table = 'Tb_Country'

class TbDeviceType(models.Model):
    id_DeviceType  = models.AutoField(db_column='id_DeviceType', primary_key=True)
    nameDeviceType = models.CharField(db_column='nameDeviceType', max_length=255 , null=False)

    def __str__(self):
        return self.nameDeviceType
    class Meta:
        managed  = True
        db_table = 'Tb_DeviceType'

class TbHwPlatform(models.Model):
    id_HwPlatform  = models.AutoField(db_column='id_HwPlatform', primary_key=True)
    nameHwPlatform = models.CharField(db_column='nameHwPlatform', max_length=255 , null=False)

    def __str__(self):
        return self.nameHwPlatform
    class Meta:
        managed  = True
        db_table = 'Tb_HwPlatform'

class TbOs(models.Model):
    id_Os  = models.AutoField(db_column='Id_Os', primary_key=True)
    nameOs = models.CharField(db_column='nameOs', max_length=255 , null=False)

    def __str__(self):
        return self.nameOs
    class Meta:
        managed  = True
        db_table = 'Tb_Os'

class TbTokenType(models.Model):
    id_TokenType  = models.AutoField(db_column='id_TokenType', primary_key=True)
    nameTokenType = models.CharField(db_column='nameTokenType', max_length=255 , null=False)

    def __str__(self):
        return self.nameTokenType
    class Meta:
        managed  = True
        db_table = 'Tb_TokenType'

class TbSettingsType(models.Model):
    id_SettingsType  = models.AutoField(db_column='id_SettingsType', primary_key=True)
    nameSettingsType = models.CharField(db_column='nameSettingsType', max_length=255 , null=False)

    def __str__(self):
        return self.nameSettingsType
    class Meta:
        managed  = True
        db_table = 'Tb_SettingsType'

# -- Entities -- #

class TbOrganization(models.Model):
    id_Organization          = models.AutoField(db_column='id_Organization', primary_key=True)
    nameOrganization         = models.CharField(db_column='nameOrganization', max_length=255 , null=False)
    taxIdOrganization        = models.CharField(db_column='taxIdOrganization', max_length=255 , null=False)
    addressOrganization      = models.CharField(db_column='addressOrganization', max_length=255 , null=False)
    contactEmailOrganization = models.CharField(db_column='contactEmailOrganization', max_length=255 , null=False)
    isActive                 = models.BooleanField(db_column= 'isActive', default=True)

    # Dependencies tables
    id_Country               = models.ForeignKey('TbCountry', db_column='id_Country' , on_delete=models.PROTECT)
    id_City                  = models.ForeignKey('TbCity', db_column='id_City', on_delete=models.PROTECT)

    def __str__(self):
        return self.nameOrganization
    class Meta:
        managed  = True
        db_table = 'Tb_Organization'

class TbSite(models.Model):
    id_Site      = models.AutoField(db_column='id_Site', primary_key=True)
    nameSite     = models.CharField(db_column='nameSite', max_length=255 , null=False)
    addressSite  = models.CharField(db_column='addressSite', max_length=255 , null=False)
    isActive     = models.BooleanField(db_column= 'isActive', default=True)

    # Dependencies tables
    id_Organization = models.ForeignKey('TbOrganization', db_column='id_Organization', on_delete=models.PROTECT)
    id_Country      = models.ForeignKey('TbCountry', db_column='id_Country' , on_delete=models.PROTECT)
    id_City         = models.ForeignKey('TbCity', db_column='id_City', on_delete=models.PROTECT)

    def __str__(self):
        return self.nameSite
    class Meta:
        managed  = True
        db_table = 'Tb_Site'

class TbZone(models.Model):
    id_Zone  = models.AutoField(db_column='id_Zone', primary_key=True)
    nameZone = models.CharField(db_column='nameZone', max_length=255 , null=False)

    # Dependencies tables
    id_Site = models.ForeignKey('TbSite', db_column='id_Site', on_delete=models.PROTECT)

    def __str__(self):
        return self.nameZone
    class Meta:
        managed  = True
        db_table = 'Tb_Zone'

class TbPeople(models.Model):
    id_People    = models.AutoField(db_column='id_People', primary_key=True)
    namePeople   = models.CharField(db_column='namePeople', max_length=255 , null=False)
    emailPeople  = models.CharField(db_column='emailPeople', max_length=255 , null=False)
    phonePeople  = models.IntegerField(db_column='phonePeople')

    # Dependencies tables
    id_Organization = models.ForeignKey('TbOrganization', db_column='id_Organization', on_delete=models.PROTECT)

    def __str__(self):
        return self.namePeople
    class Meta:
        managed  = True
        db_table = 'Tb_People'

class TbDevice(models.Model):
    id_Device           = models.AutoField(db_column='id_Device', primary_key=True)
    nameDevice          = models.CharField(db_column='nameDevice', max_length=255 , null=False)
    tokenDevice         = models.CharField(db_column='tokenDevice', max_length=255 , null=False)
    creationDateDevice  = models.DateTimeField(db_column='creationDateDevice' , null=True)

    # Dependencies tables
    id_hwPlatform   = models.ForeignKey('TbHwPlatform', db_column='id_HwPlatform', on_delete=models.PROTECT)
    id_Os           = models.ForeignKey('TbOs', db_column='id_Os', on_delete=models.PROTECT)
    id_DeviceType   = models.ForeignKey('TbDeviceType', db_column='id_DeviceType', on_delete=models.PROTECT)
    id_Organization = models.ForeignKey('TbOrganization', db_column='id_Organization', on_delete=models.PROTECT)

    def __str__(self):
        return self.nameDevice
    class Meta:
        managed  = True
        db_table = 'Tb_Device'

class TbToken(models.Model):
    id_Token   = models.AutoField(db_column='id_Token', primary_key=True)
    valueToken = models.CharField(db_column='valueToken', max_length=255 , null=False)
    id_Owner   = models.IntegerField(db_column='id_Owner' , null=False)
    # Dependencies tables
    id_TokenType = models.ForeignKey('TbTokenType', db_column='id_TokenType' , on_delete=models.PROTECT)

    def __str__(self):
        return self.valueToken
    class Meta:
        managed  = True
        db_table = 'Tb_Token'

class TbLocalization(models.Model):
    id_Localization = models.AutoField(db_column='id_Localization', primary_key=True)
    gpsDataLocation = models.CharField(db_column='gpsDataLocation', max_length=255 , null=False)
    isActive        = models.BooleanField(db_column='isActive', default=True)
    # Dependencies tables
    id_Device = models.ForeignKey('TbDevice', db_column='id_Device', on_delete=models.PROTECT)
    idZone    = models.ForeignKey('TbZone', db_column='id_Zone', on_delete=models.PROTECT)

    def __str__(self):
        return self.gpsDataLocation
    class Meta:
        managed  = True
        db_table = 'Tb_Localization'

class TbAplication(models.Model):
    id_Aplication = models.AutoField(db_column='id_Aplication', primary_key=True)
    nameAplication = models.CharField(db_column='nameAplication', max_length=255 , null=False)
    sectionAplication = models.CharField(db_column='sectionAplication', max_length= 255 , null=False)

    def __str__(self):
        return self.nameAplication
    class Meta:
        managed  = True
        db_table = 'Tb_Aplication'

class TbAutorization(models.Model):
    id_Autorization   = models.AutoField(db_column='id_Autorization', primary_key=True)
    sectionAutorization = models.CharField(db_column='sectionAutorization', max_length= 255 , null=False)
    # Dependencies tables
    id_People     = models.ForeignKey('TbPeople', db_column='id_People', on_delete=models.PROTECT)
    id_Device     = models.ForeignKey('TbDevice', db_column='id_Device', on_delete=models.PROTECT)
    id_Aplication = models.ForeignKey('TbAplication', db_column='id_Aplication', on_delete=models.PROTECT)

    def __str__(self):
        return self.sectionAutorization
    class Meta:
        managed  = True
        db_table = 'Tb_Autorization'

class TbSettings(models.Model):
    id_Settings   = models.AutoField(db_column='id_Setting', primary_key=True)
    id_Owner      = models.IntegerField(db_column='id_Owner')
    valueSettings = models.CharField(db_column='valueSettings', max_length=255 , null=False)
    # Dependencies tables
    id_SettingsType = models.ForeignKey('TbSettingsType', db_column='id_SettingsType', on_delete=models.PROTECT)

    def __str__(self):
        return self.valueSettings
    class Meta:
        managed  = True
        db_table = 'Tb_Settings'