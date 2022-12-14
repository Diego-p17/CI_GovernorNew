from ast import Try
from django.shortcuts  import render, HttpResponse, redirect
from django.contrib    import messages
from .                 import models
import folium




#------ GENERAL TABLES -------#
def get_general(request):
    #lOCATION
    tbCountry = models.TbCountry.objects.all()
    tbCity    = models.TbCity.objects.all()

    #DEVICE
    tbOs         = models.TbOs.objects.all()
    tbDeviceType = models.TbDeviceType.objects.all()
    tbHwPlatform = models.TbHwPlatform.objects.all()

    #AUTHENTICATE
    tbTokenType     = models.TbTokenType.objects.all()
    tbSettingsType  = models.TbSettingsType.objects.all()

    context = {
        'countries'     : tbCountry,
        'citys'         : tbCity,
        'operativeSys'  : tbOs,
        'deviceTypes'   : tbDeviceType,
        'Platforms'     : tbHwPlatform,
        'tokenTypes'    : tbTokenType,
        'settingsTypes' : tbSettingsType
    }

    return render(request, 'layouts/general/general.html', context)

#--country
def addCountry(request):

    if request.method == 'POST':
        nameCountry = request.POST['nameCountry'].capitalize()
        countries   = models.TbCountry.objects.filter( nameCountry = nameCountry)

        if countries:
            messages.warning(request, "Pais ya fue ingresado")
            return redirect(to='general')
        else:

            if nameCountry:
                newCountry  = models.TbCountry(nameCountry= nameCountry)
                newCountry.save()
                messages.success(request, "Pais Agregado Exitosamente")
                return redirect(to='general')
            else:
                messages.warning(request, "No se Aceptan Campos vacios")
                return redirect(to='general')

    return redirect('general.html')
def deleteCountry(request, id_Country):
    country = models.TbCountry.objects.get( id_Country=id_Country)
    if country:
        country.delete()
        messages.warning(request, "Pais eliminado")
        return redirect(to='general')
    else:
        messages.warning(request, "pais invalido")
        return redirect(to='general')
def updateCountry(request, id_Country):

    if request.method == 'POST':
        nameCountry = request.POST['nameCountry'].capitalize()
        countries = models.TbCountry.objects.filter( nameCountry = nameCountry)

    if countries:
        messages.warning(request, "Pais ya fue ingresado")
        return redirect(to='general')
    else:

        if nameCountry:
            updateCountry  = models.TbCountry.objects.get(id_Country= id_Country)
            updateCountry.nameCountry = nameCountry
            updateCountry.save()
            messages.success(request, "Pais Actualizado Exitosamente")
            return redirect(to='general')
        else:
            messages.warning(request, "No se Aceptan Campos vacios")
            return redirect(to='general')

# --City
def addCity(request):
    if request.method == 'POST':
        nameCity  = request.POST['nameCity'].capitalize()
        idCountry = request.POST['idCountry']

        city = models.TbCity.objects.filter(nameCity= nameCity, id_Country= idCountry)

        if city:
            messages.warning(request, "Ciudad ya fue ingresada")
            return redirect(to='general')
        else:
            if nameCity and idCountry != "0":
                country = models.TbCountry.objects.get(id_Country= idCountry)
                city = models.TbCity(nameCity = nameCity, id_Country = country)
                city.save()
                messages.success(request, "Ciudad Agregada Exitosamente")
                return redirect(to='general')
            else:
                messages.success(request, "Ciudad invalida")
                return redirect(to='general')
def deleteCity(request, id_City):
    city = models.TbCity.objects.get( id_City= id_City)
    if city:
        city.delete()
        messages.warning(request, "Ciudad eliminada")
        return redirect(to='general')
    else:
        messages.warning(request, "Ciudad invalida")
        return redirect(to='general')
def updateCity(request, id_City):

    if request.method == 'POST':
        nameCity  = request.POST['nameCity'].capitalize()
        idCountry = request.POST['idCountry']
        city = models.TbCity.objects.filter( nameCity = nameCity)

    if city:
        messages.warning(request, "Ciudad ya fue ingresada")
        return redirect(to='general')
    else:

        if nameCity and idCountry != '0' :
            country     = models.TbCountry.objects.get( id_Country = idCountry)
            updateCity  = models.TbCity.objects.get(id_City= id_City)
            updateCity.nameCity = nameCity
            updateCity.id_Country  = country
            updateCity.save()
            messages.success(request, "Ciudad Actualizada Exitosamente")
            return redirect(to='general')
        else:
            messages.warning(request, "Error Al actualizar")
            return redirect(to='general')

# --OS
def addOs(request):

    if request.method == 'POST':
        nameOs = request.POST['nameOs'].capitalize()
        Os = models.TbOs.objects.filter(nameOs = nameOs)

        if Os:
            messages.warning(request, "Sistema ya fue ingresada")
            return redirect(to='general')
        else:
            if nameOs:
                os = models.TbOs(nameOs = nameOs)
                os.save()
                messages.success(request, "Sistema Agregado Exitosamente")
                return redirect(to='general')
            else:
                messages.success(request, "sistema  invalido")
                return redirect(to='general')
def deleteOs(request, id_Os):
    os = models.TbOs.objects.get(id_Os= id_Os)
    if os:
        os.delete()
        messages.warning(request, "Sistema eliminado")
        return redirect(to='general')
    else:
        messages.warning(request, "sistema invalido")
        return redirect(to='general')
def updateOs(request, id_Os):
    if request.method == 'POST':
        nameOs = request.POST['nameOs'].capitalize()
        os = models.TbOs.objects.filter( nameOs = nameOs)

    if os:
        messages.warning(request, "sistema ya fue ingresado")
        return redirect(to='general')
    else:

        if nameOs:
            updateOs  = models.TbOs.objects.get(id_Os= id_Os)
            updateOs.nameOs = nameOs
            updateOs.save()
            messages.success(request, "Sistema Actualizado Exitosamente")
            return redirect(to='general')
        else:
            messages.warning(request, "No se Aceptan Campos vacios")
            return redirect(to='general')

#-- Platform
def addPlatform(request):
    if request.method == 'POST':
        namePlatform  = request.POST['namePlatform'].capitalize()
        platform      = models.TbHwPlatform.objects.filter(nameHwPlatform=namePlatform)

        if platform:
            messages.warning(request, "Plataforma ya fue ingresada")
            return redirect(to='general')
        else:
            if namePlatform:
                platform = models.TbHwPlatform(nameHwPlatform = namePlatform)
                platform.save()
                messages.success(request, "Plataforma Agregada Exitosamente")
                return redirect(to='general')
            else:
                messages.success(request, "Plataforma invalida")
                return redirect(to='general')
def deletePlatform(request, id_Platform):
    platform = models.TbHwPlatform.objects.get( id_HwPlatform= id_Platform)
    if platform:
        platform.delete()
        messages.warning(request, "plataforma eliminada")
        return redirect(to='general')
    else:
        messages.warning(request, "plataforma invalida")
        return redirect(to='general')
def updatePlatform(request, id_Platform):
    if request.method == 'POST':
        namePlatform = request.POST['namePlatform'].capitalize()
        platform = models.TbHwPlatform.objects.filter( nameHwPlatform = namePlatform)

    if platform:
        messages.warning(request, "Plataforma ya fue ingresada")
        return redirect(to='general')
    else:

        if namePlatform:
            updatePlatform  = models.TbHwPlatform.objects.get(id_HwPlatform= id_Platform)
            updatePlatform.nameHwPlatform = namePlatform
            updatePlatform.save()
            messages.success(request, "Plataforma Actualizada Exitosamente")
            return redirect(to='general')
        else:
            messages.warning(request, "No se Aceptan Campos vacios")
            return redirect(to='general')

# -- DeviceType
def addDeviceType(request):
    if request.method == 'POST':
        nameDeviceType  = request.POST['nameDeviceType'].capitalize()
        deviceType  = models.TbDeviceType.objects.filter(nameDeviceType = nameDeviceType)

        if deviceType:
            messages.warning(request, "El tipo de dispositivo ya fue ingresado")
            return redirect(to='general')
        else:
            if nameDeviceType:
                deviceType = models.TbDeviceType(nameDeviceType = nameDeviceType)
                deviceType.save()
                messages.success(request, "Tipo de Dispositivo Agregado Exitosamente")
                return redirect(to='general')
            else:
                messages.success(request, "Tipo de Dispositivo invalido")
                return redirect(to='general')
def deleteDeviceType(request, id_DeviceType):
    deviceType = models.TbDeviceType.objects.get( id_DeviceType = id_DeviceType)
    if deviceType:
        deviceType.delete()
        messages.warning(request, "Tipo de Dispositivo eliminado")
        return redirect(to='general')
    else:
        messages.warning(request, "Tipo de Dispositivo invalido")
        return redirect(to='general')
def updateDeviceType(request, id_DeviceType):
    if request.method == 'POST':
        nameDeviceType = request.POST['nameDeviceType'].capitalize()
        deviceType     = models.TbDeviceType.objects.filter( nameDeviceType = nameDeviceType)

    if deviceType:
        messages.warning(request, "Plataforma ya fue ingresada")
        return redirect(to='general')
    else:

        if nameDeviceType:
            updateDeviceType  = models.TbDeviceType.objects.get(id_DeviceType= id_DeviceType)
            updateDeviceType.nameDeviceType = nameDeviceType
            updateDeviceType.save()
            messages.success(request, "Tipo de Dispositivo Actualizada Exitosamente")
            return redirect(to='general')
        else:
            messages.warning(request, "No se Aceptan Campos vacios")
            return redirect(to='general')

#-- TokenType
def addTokenType(request):
    if request.method == 'POST':
        nameTokenType  = request.POST['nameTokenType'].capitalize()
        tokenType  = models.TbTokenType.objects.filter(nameTokenType = nameTokenType)

        if tokenType:
            messages.warning(request, "El tipo de token ya fue ingresado")
            return redirect(to='general')
        else:
            if nameTokenType:
                tokenType = models.TbTokenType(nameTokenType = nameTokenType)
                tokenType.save()
                messages.success(request, "Tipo de token Agregado Exitosamente")
                return redirect(to='general')
            else:
                messages.success(request, "Tipo de token invalido")
                return redirect(to='general')
def deleteTokenType(request, id_TokenType):
    tokenType = models.TbTokenType.objects.get( id_TokenType = id_TokenType)
    if tokenType:
        tokenType.delete()
        messages.warning(request, "Tipo de Token eliminado")
        return redirect(to='general')
    else:
        messages.warning(request, "Tipo de Token invalido")
        return redirect(to='general')
def updateTokenType(request, id_TokenType):
    if request.method == 'POST':
        nameTokenType = request.POST['nameTokenType'].capitalize()
        tokenType     = models.TbTokenType.objects.filter( nameTokenType = nameTokenType)

    if tokenType:
        messages.warning(request, "El Token ya fue ingresado")
        return redirect(to='general')
    else:

        if nameTokenType:
            updateTokenType  = models.TbTokenType.objects.get(id_TokenType= id_TokenType)
            updateTokenType.nameTokenType = nameTokenType
            updateTokenType.save()
            messages.success(request, "Tipo de token Actualizada Exitosamente")
            return redirect(to='general')
        else:
            messages.warning(request, "No se Aceptan Campos vacios")
            return redirect(to='general')

#--Settings
def addSettingsType(request):
    if request.method == 'POST':
        nameSettingsType  = request.POST['nameSettingsType'].capitalize()
        settingsType  = models.TbSettingsType.objects.filter(nameSettingsType = nameSettingsType)

        if settingsType:
            messages.warning(request, "El tipo de settings ya fue ingresado")
            return redirect(to='general')
        else:
            if nameSettingsType:
                settingsType = models.TbSettingsType(nameSettingsType = nameSettingsType)
                settingsType.save()
                messages.success(request, "Tipo de settings Agregado Exitosamente")
                return redirect(to='general')
            else:
                messages.success(request, "Tipo de settings invalido")
                return redirect(to='general')
def deleteSettingsType(request, id_SettingsType):
    settingsType = models.TbSettingsType.objects.get( id_SettingsType = id_SettingsType)
    if settingsType:
        settingsType.delete()
        messages.warning(request, "Tipo de settings eliminado")
        return redirect(to='general')
    else:
        messages.warning(request, "Tipo de settings invalido")
        return redirect(to='general')
def updateSettingsType(request, id_SettingsType):
    if request.method == 'POST':
        nameSettingsType = request.POST['nameSettingsType'].capitalize()
        settingsType     = models.TbSettingsType.objects.filter( nameSettingsType = nameSettingsType)

    if settingsType:
        messages.warning(request, "El tipo de settings ya fue ingresado")
        return redirect(to='general')
    else:

        if nameSettingsType:
            updateSettingsType  = models.TbSettingsType.objects.get(id_SettingsType= id_SettingsType)
            updateSettingsType.nameSettingsType = nameSettingsType
            updateSettingsType.save()
            messages.success(request, "Tipo de Settings Actualizado Exitosamente")
            return redirect(to='general')
        else:
            messages.warning(request, "No se Aceptan Campos vacios")
            return redirect(to='general')

#-------------------#
#   Organizations   #
#-------------------#

def getAllOrganizations(request):
    organizations = models.TbOrganization.objects.all().exclude(nameOrganization = "sin organizacion")
    citys         = models.TbCity.objects.all()
    countries     = models.TbCountry.objects.all()
    context       = {
                     "organizations": organizations,
                     "citys"        : citys,
                     "countries"    : countries
                    }
    return render(request, 'layouts/organization/organizations.html', context)
def getOrganization(request, id_Organization):
    # General Tables
    countries = models.TbCountry.objects.all()
    citys     = models.TbCity.objects.all()

    organization   = models.TbOrganization.objects.get(id_Organization = id_Organization)
    peoplesOrg     = models.TbPeople.objects.filter(id_Organization = id_Organization)
    sitesOrg       = models.TbSite.objects.filter(id_Organization = id_Organization)
    idOrganization = organization.id_Organization
    #verify people with  emptyOrganization
    emptyOrg     = models.TbOrganization.objects.get(nameOrganization = 'sin organizacion')
    idEmptyOrg   = emptyOrg.id_Organization
    peoples      = models.TbPeople.objects.filter(id_Organization = idEmptyOrg).values('id_People','namePeople','id_Organization')
    sites        = models.TbSite.objects.filter(id_Organization = idEmptyOrg).values('id_Site', 'nameSite','id_Organization')

    devices = []
    for site in sites:
        id_site = site.get('idSite')
        zones = models.TbZone.objects.filter(id_Site = id_site)
        for zone in zones:
            id_zone = zone.get('idZone')
            device = models.TbDevice.objects.filter(id_Zone = id_zone)
            devices.append(device)



    context = {
               "idOrganization": idOrganization,
               "organization"  : organization,
               "peoplesOrg"    : peoplesOrg,
               "peoples"       : peoples,
               "sitesOrg"      : sitesOrg,
               "sites"         : sites,
               "devices"       : devices,
               "countries"     : countries,
               "citys"         : citys
              }

    return render(request, 'layouts/organization/organization_info.html', context)
def addOrganization(request):
    if request.method == 'POST':
        nameOrg    = request.POST['nameOrg']
        taxIdOrg   = request.POST['taxIdOrg']
        countryOrg = request.POST['countryOrg']
        cityOrg    = request.POST['cityOrg']
        addressOrg = request.POST['addressOrg']
        emailOrg   = request.POST['emailOrg']

        country      = models.TbCountry.objects.get(id_Country= countryOrg)
        city         = models.TbCity.objects.get(id_City= cityOrg)
        organization = models.TbOrganization.objects.filter(nameOrganization = nameOrg)

        if organization:
            messages.warning(request, "La organizacion ya fue ingresada")
            return redirect(to='home')
        else:
            #instance new organization
            new_organization = models.TbOrganization(nameOrganization = nameOrg, taxIdOrganization = taxIdOrg, id_Country = country, id_City = city, addressOrganization = addressOrg, contactEmailOrganization = emailOrg)
            new_organization.save()
            messages.success(request, "Organizacion ingresada exitosamente")
            return redirect(to='home')
    else:
        return redirect(to='home')


# Delete organization --------------------------------------------------------------------------------------
def deleteOrganization(request, id_Organization):
    organization = models.TbOrganization.objects.get( id_Organization = id_Organization)

    if organization:
        messages.success(request, "Organizaci??n eliminada exitosamente")
        organization.delete()
        return redirect(to= 'home')
    else:
        messages.warning(request, "Organizacion no encontrada")
        return redirect(to='home')


def updateOrganization(request, id_Organization):

    if request.method == 'POST':

        nameOrganization = request.POST['nameOrg']
        taxId            = request.POST['taxId']
        address          = request.POST['adressOrg']
        city             = request.POST['cityOrg']
        country          = request.POST['countryOrg']

        organization      = models.TbOrganization.objects.get( id_Organization = id_Organization)
        organizationCheck = models.TbOrganization.objects.filter( nameOrganization = nameOrganization).exclude( id_Organization = id_Organization)

        if organization.nameOrganization == nameOrganization and organization.taxIdOrganization == taxId and organization.addressOrganization == address and organization.id_Country.id_Country == int(country) and organization.id_City.id_City == int(city):
            messages.warning(request, "No se ha modificado ningun valor")
            return redirect( 'organization' , id_Organization )
        elif  organizationCheck:
            messages.warning(request, "Ya existe una organizacion con el mismo nombre")
            return redirect( 'organization' , id_Organization )
        else:
            country      = models.TbCountry.objects.get( id_Country= int(country) )
            city         = models.TbCity.objects.get( id_City= int(city) )

            organization.nameOrganization    = nameOrganization
            organization.taxIdOrganization   = taxId
            organization.addressOrganization = address
            organization.id_City             = city
            organization.id_Country          = country

            organization.save()

            messages.success(request, "La Organizacion fue actualizada con exito")
            return redirect( 'organization' , id_Organization )
def addPeopleOrg(request, id_Organization):
    if request.method == 'POST':

        id_People     = request.POST['people']
        organization  = models.TbOrganization.objects.get(id_Organization = id_Organization)
        people        = models.TbPeople.objects.get(id_People = id_People)

        people.id_Organization = organization
        people.save()
        messages.success(request, "Persona Agregada Exitosamente")
        return redirect('organization', id_Organization)
    else:
        messages.error(request, "Ha Ocurrido Un error Inesperado")
        return redirect('organization', id_Organization)
def deletePeopleOrg(request, id_People):

    emptyOrganization = models.TbOrganization.objects.get(nameOrganization = 'sin organizacion')
    people            = models.TbPeople.objects.get(id_People = id_People)
    idOrganization    = people.id_Organization.id_Organization

    if  emptyOrganization:
        if people:
            people.id_Organization = emptyOrganization
            people.save()
            messages.success(request, "La persona fue retirada de la organizacion")
            return redirect('organization', idOrganization)
        else:
            messages.error(request, "Persona No encontrada")
            return redirect('organization', idOrganization)
    else:
        messages.error(request, "Ha ocurrido un error al eliminar la persona")
        return redirect('organization', idOrganization)

def addSiteOrg(request, id_Organization):

    if request.method == 'POST':

        id_Site       = int(request.POST['site'])
        organization  = models.TbOrganization.objects.get(id_Organization = id_Organization)
        site          = models.TbSite.objects.get(id_Site = id_Site)

        site.id_Organization = organization
        site.save()
        messages.success(request, "Sitio Agregado Exitosamente")
        return redirect('organization', id_Organization)
    else:
        messages.error(request, "Ha Ocurrido Un error Inesperado")
        return redirect('organization', id_Organization)
def deleteSiteOrg(request, id_Site):

    emptyOrganization = models.TbOrganization.objects.get(nameOrganization = 'sin organizacion')
    site              = models.TbSite.objects.get(id_Site = id_Site)
    idOrganization    = site.id_Organization.id_Organization

    if  emptyOrganization:
        if site:
            site.id_Organization = emptyOrganization
            site.save()
            messages.success(request, "El Sitio fue retirado de la organizacion")
            return redirect('organization', idOrganization)
        else:
            messages.error(request, "Sitio No encontrado")
            return redirect('organization', idOrganization)
    else:
        messages.error(request, "Ha ocurrido un error al eliminar el sitio")
        return redirect('organization', idOrganization)


#-------------#
#    Sites    #
#-------------#

def getAllSites(request):
    sites         = models.TbSite.objects.all()
    organizations = models.TbOrganization.objects.all()
    citys         = models.TbCity.objects.all()
    countries     = models.TbCountry.objects.all()
    context       = {
                     'sites'         :sites,
                     'organizations' :organizations,
                     'citys'         :citys,
                     'countries'     :countries
                     }
    return render(request, 'layouts/site/sites.html', context)
def getSite(request, id_Site):

    site          = models.TbSite.objects.get(id_Site = id_Site)
    zones         = models.TbZone.objects.filter(id_Site = id_Site)
    countries     = models.TbCountry.objects.all()
    citys         = models.TbCity.objects.all()
    organizations = models.TbOrganization.objects.all()
    context = {
                "site"          :site,
                "zones"         :zones,
                "countries"     :countries,
                "citys"         :citys,
                "organizations" :organizations
              }

    return render(request, 'layouts/site/site_info.html', context)


def addSite(request):
    if request.method == 'POST':

        nameSite        = request.POST['nameSite'].capitalize()
        countrySite     = request.POST['countrySite']
        citySite        = request.POST['citySite']
        addressSite     = request.POST['addressSite']
        idOrganization  = request.POST['organization']

        site = models.TbSite.objects.filter(nameSite= nameSite , id_Organization= idOrganization)
        if site:
            messages.warning(request, 'el sitio ya fue agregado')
            return redirect(to='sites')
        else:
            countrySite  =  models.TbCountry.objects.get(id_Country= countrySite)
            citySite     =  models.TbCity.objects.get(id_City= citySite)
            organization =  models.TbOrganization.objects.get(id_Organization= idOrganization)
            site = models.TbSite(nameSite = nameSite, id_Country = countrySite, id_City = citySite, addressSite = addressSite, id_Organization = organization)
            site.save()
            messages.success(request, 'el sitio ya fue agregado')
            return redirect(to='sites')
def updateSite(request, id_Site):
    if request.method == 'POST':

        nameSite        = request.POST['nameSite'].capitalize()
        countrySite     = request.POST['countrySite']
        citySite        = request.POST['citySite']
        addressSite     = request.POST['addressSite']
        id_Organization = request.POST['organization']

        site       = models.TbSite.objects.get(id_Site =id_Site)
        siteCheck  = models.TbSite.objects.filter(nameSite = nameSite, id_Organization = id_Organization).exclude(id_Site=id_Site)

        if  site.nameSite == nameSite and site.id_Country.id_Country == int(countrySite) and site.id_City.id_City == int(citySite) and site.id_Organization.id_Organization == int(id_Organization) and site.addressSite  == addressSite:
            messages.warning(request, "ingrese nuevos valores validos")
            return redirect('site', id_Site)

        elif siteCheck:
            messages.warning(request, "el sitio ya existe")
            return redirect('site', id_Site)

        else:
            organization = models.TbOrganization.objects.get(id_Organization= id_Organization)
            countrySite      = models.TbCountry.objects.get(id_Country = countrySite)
            citySite         = models.TbCity.objects.get(id_City = citySite)

            site.nameSite        = nameSite
            site.id_Country      = countrySite
            site.id_City         = citySite
            site.addressSite     = addressSite
            site.id_Organization = organization
            site.save()

            messages.success(request, "Informacion actualizada")
            return redirect('site', id_Site)
def addZone(request, id_Site):

    if request.method == 'POST':
        nameZone = request.POST['nameZone'].capitalize()
        zones    = models.TbZone.objects.filter(id_Site = id_Site)
        site     = models.TbSite.objects.get(id_Site = id_Site)

        zoneCheck = models.TbZone.objects.filter(id_Site = id_Site, nameZone = nameZone)

        if zoneCheck:
            messages.warning(request, "La zona Ingresada ya existe")
            return redirect('site', id_Site)

        else:

            zone = models.TbZone(nameZone = nameZone, id_Site = site)
            zone.save()

            messages.success(request, "Zona Agregada exitosamente")
            return redirect('site', id_Site)

    else:
        return redirect('site', id_Site)
def updateZone(request, id_Zone):
    if request.method == 'POST':
        nameZone  = request.POST['nameZone']
        zone      = models.TbZone.objects.get(id_Zone = id_Zone)
        id_Site   = zone.id_Site.id_Site
        zoneCheck = models.TbZone.objects.filter( nameZone = nameZone , id_Site = zone.id_Site)

        if zoneCheck:
            messages.warning(request, "La zona Ingresada ya existe")
            return redirect('site', id_Site)
        elif  nameZone == zone.nameZone:
            messages.warning(request, "Ingrese un Dato Nuevo")
            return redirect('site', id_Site)

        else:
            zone.nameZone = nameZone
            zone.save()
            messages.success(request, "Zona Actualizada")
            return redirect('site', id_Site)

    else:
        return redirect('site', id_Site)
def deleteZone(request, id_Zone):
    try:
        zone    = models.TbZone.objects.get(id_Zone = id_Zone)
        id_Site = zone.id_Site.id_Site
        if zone:
            zone.delete()
            messages.success(request, "Zona eliminada")
            return redirect('site', id_Site)
    except:
        messages.success(request, "ha ocurrido un error ")
        return redirect('sites')

#-------------#
#   Peoples   #
#-------------#

def getPeoples(request):
    peoples       = models.TbPeople.objects.all()
    organizations = models.TbOrganization.objects.all()
    context = {'peoples':peoples, 'organizations':organizations}
    return render(request, 'layouts/people/peoples.html', context)
def peopleInfo(request, id_People):
    people         = models.TbPeople.objects.get(id_People = id_People)
    organizations  = models.TbOrganization.objects.all()
    idOrganization = models.TbOrganization.objects.get(id_Organization = people.id_Organization.id_Organization )

    context = {
               "people"         : people,
               "organizations"  : organizations,
               "idOrganization" : idOrganization.id_Organization,
              }

    return render(request, 'layouts/people/people_info.html', context)
def addPeople(request):
    if request.method == 'POST':
        namePeople      = request.POST['namePeople']
        emailPeople     = request.POST['emailPeople']
        phonePeople     = request.POST['phonePeople']
        id_Organization = request.POST['organization']

        organization = models.TbOrganization.objects.get(id_Organization = id_Organization)

        if organization:
            newPeople = models.TbPeople( namePeople= namePeople , emailPeople = emailPeople, phonePeople = phonePeople, id_Organization = organization)
            newPeople.save()
            messages.success( request, 'Persona agregada Exitosamente')
            return redirect(to='peoples')
        else:
            messages.warning(request, 'valide la informacion ingresada')
            return redirect(to='peoples')
    else:
        return redirect(to='peoples')
def updatePeople(request, id_People):
    if request.method == 'POST':
        namePeople     = request.POST['namePeople']
        emailPeople    = request.POST['emailPeople']
        phonePeople    = int(request.POST['phonePeople'])
        idOrganization = int(request.POST['orgPeople'])

        people = models.TbPeople.objects.get(id_People = id_People)

        if people:
            if namePeople == people.namePeople and  emailPeople == people.emailPeople and phonePeople == people.phonePeople and idOrganization == people.id_Organization.id_Organization :
                messages.success( request, 'ingrese nuevos datos para actualizar' )
                return redirect('people', id_People)

            else:

                organization           = models.TbOrganization.objects.get(id_Organization = idOrganization)
                people.namePeople      = namePeople
                people.emailPeople     = emailPeople
                people.phonePeople     = phonePeople
                people.id_Organization = organization
                people.save()
                messages.success( request, 'actualizado Correctamente' )
                return redirect('people', id_People)
        else:
            messages.warning( request, 'ha ocurrido un error al actualizar')
            return redirect('peopleInfo', id_People)
def deletePeople(request, id_People):

    people = models.TbPeople.objects.get(id_People = id_People)
    if people:
        people = people.delete()
        messages.success( request, 'ha sido eliminado exitosamente')
        return redirect(to='peoples')
    else:
        messages.warning( request, 'ha ocurrido un error al eliminar')
        return redirect(to='peoples')


#----------------#
#     Devices    #
#----------------#

# show all devices
def getAllDevices(request):

    devices = models.TbDevice.objects.all()

    hwPlatforms   = models.TbHwPlatform.objects.all()
    typeDevices   = models.TbDeviceType.objects.all()
    osDevices     = models.TbOs.objects.all()
    organizations = models.TbOrganization.objects.all()
    zones         = models.TbZone.objects.all()

    context = {'devices':devices, "hwPlatforms":hwPlatforms, "typeDevices":typeDevices, "osDevices":osDevices, "organizations":organizations, "zones":zones}

    return render(request, 'layouts/device/device.html', context)

def getDevice(request, id_Device):

    device    = models.TbDevice.objects.get(id_Device = id_Device)
    parseDate = device.creationDateDevice.strftime('%Y-%m-%d')
    device.creationDateDevice = parseDate
    hwPlatforms   = models.TbHwPlatform.objects.all()
    typeDevices   = models.TbDeviceType.objects.all()
    osDevices     = models.TbOs.objects.all()
    organizations = models.TbOrganization.objects.all()

    sites     = models.TbSite.objects.filter(id_Organization = device.id_Organization)

    zonesList = []
    for site in sites:
        zones = models.TbZone.objects.filter(id_Site = site.id_Site)
        for zone in zones:
            zonesList.append(zone)

    localization = models.TbLocalization.objects.filter(id_Device = id_Device , isActive = True )

    if localization:
        localization = models.TbLocalization.objects.get(id_Device = id_Device , isActive = True )
        localization = localization.gpsDataLocation.split(",")
    else:
        localization = [0,0]


    location = getLocation(device)
    historyDevice = getHistoryLocation(id_Device)

    context = {
                "device"        :device,
                "hwPlatforms"   :hwPlatforms,
                "typeDevices"   :typeDevices,
                "osDevices"     :osDevices,
                "organizations" :organizations,
                "zones"         :zonesList,
                "location"      :location,
                "history"       :historyDevice,
                "cordinate_x"   :localization[0] ,
                "cordinate_y"   :localization[1] }

    return render(request, 'layouts/device/device_info.html', context)

def getLocation(device):

    localization = models.TbLocalization.objects.filter(id_Device=device.id_Device).exclude(isActive = False)

    if  localization:
        for location in localization:
            cordinates  = location.gpsDataLocation.split(',')
            cordinate_x = cordinates[0]
            cordinate_y = cordinates[1]

            map = folium.Map(location=[cordinate_x, cordinate_y], zoom_start=25)
            folium.Marker(
                        location = [cordinate_x, cordinate_y],
                        popup    = f"<i>{device.id_Organization}</i>",
                        tooltip  = "informacion"
                        ).add_to(map)
    else:
        map = folium.Map()

    map = map._repr_html_()
    return map
def getHistoryLocation(id_Device):
    try:
        localization = models.TbLocalization.objects.filter(id_Device = id_Device , isActive = False)
        return localization
    except:
        return None
def addLocation(request, id_Device):

    if request.method == "POST":
        cordinate_x = float(request.POST['cordinate-x'])
        cordinate_y = float(request.POST['cordinate-y'])
        zoneDevice  = int(request.POST['zone'])

        device = models.TbDevice.objects.get(id_Device =id_Device)
        zone   = models.TbZone.objects.get(id_Zone =zoneDevice)
        gpsDataLocation = f"{cordinate_x},{cordinate_y}"

        locationCheck = models.TbLocalization.objects.filter(id_Device = id_Device , isActive = True)

        if locationCheck:
            locationCheck = models.TbLocalization.objects.get(id_Device = id_Device , isActive = True)
            locationCheck.isActive = False
            locationCheck.save()

        if zoneDevice == 0 :
            messages.warning(request, "el sitio no tiene zonas agregadas")
            return redirect('device', id_Device)

        elif device:
            location = models.TbLocalization( gpsDataLocation = gpsDataLocation, id_Zone = zone, id_Device= device)
            location.save()
            messages.success(request, "localizacion agregada correctamente")
            return redirect('device', id_Device)

        else:
            messages.warning(request, "dispositivo no existe")
            return redirect('device', id_Device)


# add device
def addDevice(request):

    if request.method == 'POST':
        nameDevice   = request.POST['nameDevice']
        tokenDevice  = request.POST['tokenDevice']
        creationDate = request.POST['creationDateDevice']
        hwPlatform   = int(request.POST['hwPlatform'])
        typeDevice   = int(request.POST['typeDevice'])
        osDevice     = int(request.POST['osDevice'])
        organization = int(request.POST['organization'])

        deviceCheck = models.TbDevice.objects.filter( nameDevice = nameDevice , id_Organization = organization)
        if deviceCheck:
            messages.warning( request, 'EL dispositivo ya existe')
            return redirect(to='devices')

        else:
            #foreignKeys
            idHwPlatform   = models.TbHwPlatform.objects.get(id_HwPlatform = hwPlatform)
            idTypeDevice   = models.TbDeviceType.objects.get(id_DeviceType = typeDevice)
            idOsDevice     = models.TbOs.objects.get(id_Os = osDevice)
            idOrganization = models.TbOrganization.objects.get(id_Organization = organization)

            newDevice = models.TbDevice(nameDevice = nameDevice, tokenDevice = tokenDevice , creationDateDevice = creationDate,  id_DeviceType = idTypeDevice, id_HwPlatform = idHwPlatform , id_Os = idOsDevice, id_Organization = idOrganization)
            newDevice.save()
            messages.success( request, 'Dispositivo Ingresado')
            return redirect(to='devices')

    messages.warning( request, 'Ha Ocurrido un error inesperado')
    return redirect(to='devices')
def updateDevice(request, id_Device):
    if request.method == 'POST':
        nameDevice   = request.POST['nameDevice']
        tokenDevice  = request.POST['tokenDevice']
        creationDate = request.POST['creationDateDevice']
        hwPlatform   = int(request.POST['hwPlatform'])
        typeDevice   = int(request.POST['typeDevice'])
        osDevice     = int(request.POST['osDevice'])
        organization = int(request.POST['organization'])

        deviceCheck = models.TbDevice.objects.filter( nameDevice = nameDevice , id_Organization = organization).exclude(id_Device = id_Device)
        if deviceCheck:
            messages.warning( request, 'EL dispositivo ya existe')
            return redirect( 'device' , id_Device)
        else:
            device = models.TbDevice.objects.get(id_Device = id_Device)
            if device.nameDevice == nameDevice and device.tokenDevice == tokenDevice and device.creationDateDevice == creationDate and device.id_HwPlatform.id_HwPlatform == hwPlatform and device.id_DeviceType.id_DeviceType == typeDevice and device.id_Os.id_Os == osDevice and device.id_Organization.id_Organization == organization:
                messages.warning( request, 'ingrese valores distintos')
                return redirect( 'device' , id_Device)
            else:
                #foreignKeys
                idHwPlatform   = models.TbHwPlatform.objects.get(id_HwPlatform = hwPlatform)
                idTypeDevice   = models.TbDeviceType.objects.get(id_DeviceType = typeDevice)
                idOsDevice     = models.TbOs.objects.get(id_Os = osDevice)
                idOrganization = models.TbOrganization.objects.get(id_Organization = organization)

                device.nameDevice         = nameDevice
                device.tokenDevice        = tokenDevice
                device.creationDateDevice = creationDate
                device.id_HwPlatform      = idHwPlatform
                device.id_DeviceType      = idTypeDevice
                device.id_Os              = idOsDevice
                device.id_Organization    = idOrganization

                device.save()

                messages.success( request, 'Dispositivo Actualizado')
                return redirect( 'device' , id_Device)

    messages.warning( request, 'Ha Ocurrido un error inesperado')
    return redirect(to='devices')


# Eliminar dispostivos atravez de la interfaz
def delete_device(request, idDevice):


    device = models.TbDevice.objects.get(id_Device = idDevice)
    device.delete()

    return redirect('devices')

#--------------------#
#   Authorizations   #
#--------------------#
def getAllAuthorizations(request):

    device = models.TbDevice.objects.all()
    people = models.TbPeople.objects.all()

    return render(request, 'layouts/authorization/authorizations.html',{})


def getAllAplications(request):
    aplications = models.TbAplication.objects.all()
    context = { 'aplications':aplications }
    return render(request , 'layouts/aplication/aplications.html', context)
def addAplication(request):

    if request.method == 'POST':
        nameAplication = request.POST['nameAplication'].capitalize()
        nameCheck      = models.TbAplication.objects.filter(nameAplication = nameAplication)

        if nameCheck:
            messages.warning( request, 'aplicacion ya existe')
            return redirect( 'aplications')
        else:
            aplication = models.TbAplication(nameAplication = nameAplication)
            aplication.save()
            messages.success( request, 'aplicacion agregada')
            return redirect( 'aplications')

def getAplication(request, id_Aplication):
    try:
        aplication = models.TbAplication.objects.get(id_Aplication =id_Aplication)
        submodules = models.TbSubModule.objects.filter(id_Aplication = id_Aplication)

        context = { "aplication": aplication, "submodules": submodules}
        return  render(request, 'layouts/aplication/aplication_info.html', context)
    except Exception as e:
        print(e)
        messages.error( request, 'ha ocurrido un error')
        return redirect( 'aplications')
    pass
def addSubmodule(request, id_Aplication):
    if request.method == 'POST':
        nameSubModule         = request.POST['nameSubModule']
        descriptionSubModule  = request.POST['descriptionSubModule']

        subModuleCheck = models.TbSubModule.objects.filter(nameSubModule = nameSubModule)
        try:
            if subModuleCheck:
                messages.warning(request, "El Sub-Modulo ya existe" )
                return redirect( 'aplication', id_Aplication)
            else:
                aplication = models.TbAplication.objects.get(id_Aplication = id_Aplication)
                subModule  = models.TbSubModule(nameSubModule = nameSubModule, descriptionSubModule = descriptionSubModule, id_Aplication = aplication)
                subModule.save()
                messages.success(request, "El Sub-Modulo fue agregado" )
                return redirect( 'aplication', id_Aplication)
        except Exception as e:
            print(e)
            messages.warning(request, "Ha Ocurrido un Error")
            return redirect( 'aplication', id_Aplication)

def updateSubModule(request, id_SubModule):
    if request.method == 'POST':
        nameSubModule = request.POST['nameSubModule']
        descriptionSubModule  = request.POST['descriptionSubModule']

        subModuleCheck = models.TbSubModule.objects.filter(nameSubModule = nameSubModule)
        subModule      = models.TbSubModule.objects.get(id_SubModule = id_SubModule)
        try:
            if subModuleCheck:
                messages.warning(request, "El Sub-Modulo ya existe" )
                return redirect( 'aplication', subModule.id_Aplication)
            elif subModule.nameSubModule == nameSubModule and subModule.descriptionSubModule == descriptionSubModule:
                messages.warning(request, "Ingrese Nuevos datos" )
                return redirect( 'aplication', subModule.id_Aplication)
            else:
                aplication = models.TbAplication.objects.get(id_Aplication = subModule.id_Aplication)
                subModule.nameSubModule        = nameSubModule
                subModule.descriptionSubModule = descriptionSubModule
                subModule.save()
                messages.success(request, "El Sub-Modulo Actualizado" )
                return redirect( 'aplication', subModule.id_Aplication)
        except Exception as e:
            print(e)
            messages.warning(request, "Ha Ocurrido un Error")
            return redirect( 'aplication', subModule.id_Aplication)

def deleteSubModule(request, id_SubModule):
    try:
        subModule = models.TbSubModule.objects.get(id_SubModule = id_SubModule)
        id_Aplication = subModule.id_Aplication.id_Aplication

        if subModule:
            subModule.delete()
            messages.success(request, "El Sub-Modulo ha sido eliminado")
            return redirect( 'aplication', id_Aplication)

        else:
            messages.warning(request, "El Sub-Modulo no encontrado")
            return redirect( 'aplication', id_Aplication)
    except Exception as e:
        print(e)
        messages.warning(request, "Ha Ocurrido un error")
        return redirect( 'aplications')

#------------------------------------------------------------------------------
# Muestra los permisos relacionados a la persona seleccionada persona
def permisos_persona(request, id_persona):

    persona  = models.tb_people.objects.get(email_people = id_persona)
    permisos = models.tb_permissions.objects.filter(email_people = id_persona)
    context  = {"permisos": permisos, "persona":persona.name_people, "email":id_persona}

    return render(request, 'personas/permisos_persona.html', context)

def eliminar_permiso(request, id_persona, id_permiso):

    permiso = models.tb_permissions.objects.get(id_permission = id_permiso)
    permiso.delete()

    return redirect('permisos_persona', id_persona)

def modificar_permiso(request, id_persona, id_permiso):

    orgs  = models.tb_org.objects.all()
    sites = models.tb_sites.objects.all()
    zones = models.tb_zones.objects.all()

    permiso = models.tb_permissions.objects.get(id_permission = id_permiso)

    org_  = models.tb_org.objects.get(org_name = permiso.id_org)
    site_ = models.tb_sites.objects.get(site_name = permiso.id_site)
    zone_ = models.tb_zones.objects.get(zone_name = permiso.id_zone)

    var = permiso.level

    context = {"orgs":orgs, "sites":sites, "zones":zones, "permiso":permiso, "org":org_, "site":site_, "zone":zone_, "var":var, "email": id_persona, "id_permiso":id_permiso}

    return render(request, 'personas/formulario_actualizar_permiso.html', context)

def guardar_modificar_permiso(request, id_persona, id_permiso):

    org     = request.POST.get('org')
    site    = request.POST.get('site')
    zone    = request.POST.get('zone') 
    level   = request.POST.get('permiso')

    org_    = models.tb_org.objects.get(id_org = org)
    site_   = models.tb_sites.objects.get(id_site = site)
    zone_   = models.tb_zones.objects.get(id_zone = zone)
    people_ = models.tb_people.objects.get(email_people = id_persona)

    permiso         = models.tb_permissions.objects.get(id_permission = id_permiso)
    permiso.id_org  = org_
    permiso.id_site = site_
    permiso.id_zone = zone_
    permiso.level   = level
    permiso.save()

    return redirect('permisos_persona', id_persona)

# Envia al formulario para asignar nuevos permisos a una persona
def formulario_permisos(request, id_persona):

    org   = models.tb_org.objects.all()
    sites = models.tb_sites.objects.all()
    zones = models.tb_zones.objects.all()

    #print(id_persona)
    context = {"org":org, "sites":sites, "zones":zones, "email": id_persona}

    return render(request, 'personas/formulario_permisos_persona.html', context)

# Guarda el permiso asignado el id de la persona
def guardar_permiso(request, id_persona):

    org     = request.POST.get('org')
    site    = request.POST.get('site')
    zone    = request.POST.get('zone')
    level   = request.POST.get('permiso')

    org_    = models.tb_org.objects.get(id_org = org)
    site_   = models.tb_sites.objects.get(id_site = site)
    zone_   = models.tb_zones.objects.get(id_zone = zone)
    people_ = models.tb_people.objects.get(email_people = id_persona)

    permiso = models.tb_permissions(email_people = people_, id_org = org_, id_site = site_, id_zone = zone_, level = level)
    permiso.save()

    return redirect('tabs_personas', id_persona)

#------------------------------------------------------------------------------

