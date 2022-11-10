from django.shortcuts  import render, HttpResponse, redirect
from django.contrib    import messages
from .                 import models




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

    return render(request, 'general.html', context)

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

#Show all organizations
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

#show all data the organization
def getOrganization(request, idOrg):

    organization   = models.TbOrganization.objects.filter(id_Organization = idOrg)
    idOrganization = organization[0]['id_Organization']
    peoplesOrg     = models.TbPeople.objects.filter(id_Organization = idOrg)
    sitesOrg       = models.TbSite.objects.filter(id_Organization = idOrg)


    #verify people with  emptyOrganization
    emptyOrg     = models.TbOrganization.objects.filter(nameOrganization = 'sin organizacion').values('id_Organization')
    idEmptyOrg   = emptyOrg[0]['id_Organization']
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
               "organization":   organization,
               "peoplesOrg":     peoplesOrg,
               "peoples":        peoples,
               "sitesOrg":       sitesOrg,
               "sites":          sites,
               "devices":        devices,
              }

    return render(request, 'organizations/organization_info.html', context)

# Add new Organization
def addOrganization(request):

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

# Delete organization --------------------------------------------------------------------------------------
def deleteOrganization(request, idOrg):
    organization = models.TbOrganization.objects.get( id_Organization = idOrg)

    if organization:
        messages.success(request, "Organización eliminada exitosamente")
        organization.delete()
        return redirect(to= 'home')
    else:
        messages.warning(request, "Organizacion no encontrada")
        return redirect(to='home')

#Update Data Organization
def update_organization(request, idOrg):

    organization = models.Organizations.objects.get( idOrganization = idOrg)

    nameOrganization = request.POST['nameOrg']
    taxId            = request.POST['taxId']
    postal           = request.POST['postalOrg']
    address          = request.POST['adressOrg']
    city             = request.POST['cityOrg']
    country          = request.POST['countryOrg']

    organization.nameOrganization    = nameOrganization
    organization.taxIdOrganization   = taxId
    organization.postalOrganization  = postal
    organization.addressOrganization = address
    organization.cityOrganization    = city
    organization.countryOrganization = country

    organization.save()

    return redirect('organization', idOrg)

#Add people at the  organization
def add_peopleOrg(request, idOrg):

    idPeople     = request.POST['people']
    organization = models.Organizations.objects.get(idOrganization = idOrg)
    people       = models.Peoples.objects.get(idPeople = idPeople)

    people.organizations_idOrganization_id = organization
    people.save()

    return redirect('organization', idOrg)

#Add site at the organization
def add_siteOrg(request, idOrg):


    organization = models.Organizations.objects.get(idOrganization = idOrg)
    idSite       = request.POST['site']
    site         = models.Sites.objects.get(idSite = idSite)
    site.organizations_idOrganization_id = organization
    site.save()

    return redirect('organization', idOrg)

# Delete Site the organization
def delete_orgSite(request, idSite):
    empty_organization = models.Organizations.objects.get(nameOrganization = 'sin organizacion')
    site = models.Sites.objects.get(idSite = idSite)
    idOrganization = site.organizations_idOrganization_id
    print(idOrganization)
    site.organizations_idOrganization_id = empty_organization
    site.save()

    return redirect('organization', idOrganization)

#Delete People at the organization
def delete_peopleOrg(request, idPeople , idOrganization):
    empty_organization = models.Organizations.objects.get(nameOrganization = 'sin organizacion')
    people             = models.Peoples.objects.get(idPeople = idPeople)
    idOrganization     = people.organizations_idOrganization_id
    people.organizations_idOrganization = empty_organization
    people.save()

    return redirect('organization', idOrganization)



#-------------#
#    Sites    #
#-------------#

# show all sites
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

# show all data the site
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

    return render(request, 'sites/site_info.html', context)

#add site
def addSite(request):
    if request.method == 'POST':

        nameSite        = request.POST['nameSite']
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

#update Site
def updateSite(request, id_Site):
    if request.method == 'POST':

        nameSite        = request.POST['nameSite']
        countrySite     = request.POST['countrySite']
        citySite        = request.POST['citySite']
        addressSite     = request.POST['addressSite']
        id_Organization = request.POST['id_Organization']

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


#add zone the site
def add_zone(request, idSite):
    site     = models.Sites.objects.filter(idSite = idSite).values('idSite')
    nameZone = request.POST['nameZone']
    zone     = models.Zones(nameZone = nameZone, sites_idSite_id = site)
    zone.save()
    return redirect('site_info', idSite)

#update zone the site
def update_zone(request, idZone):
    zone     = models.Zones.objects.get(idZone = idZone)
    nameZone = request.POST['nameZone']
    idSite   = zone.sites_idSite_id
    zone.nameZone = nameZone

    zone.save()

    return redirect('site_info', idSite)

#delete zone the site
def delete_zone(request, idZone):
    zone     = models.Zones.objects.get(idZone = idZone)
    idSite   = zone.sites_idSite_id
    zone.delete()

    return redirect('site_info', idSite)

#view form add site
def form_site(request):
    organizations = models.Organizations.objects.all().values('idOrganization', 'nameOrganization')
    context = { 'organizations':organizations}

    return render(request, 'sites/form_site.html', context)


#-------------#
#   Peoples   #
#-------------#

# Show all peoples
def getPeoples(request):
    peoples       = models.TbPeople.objects.all()
    organizations = models.TbOrganization.objects.all()
    context = {'peoples':peoples, 'organizations':organizations}
    return render(request, 'layouts/people/peoples.html', context)

# show data people information
def peopleInfo(request, id_People):
    people         = models.TbPeople.objects.get(id_People = id_People)
    organizations  = models.TbOrganization.objects.all()
    idOrganization = models.TbOrganization.objects.get(id_Organization = people.id_Organization.id_Organization )

    context = {
               "people"         : people,
               "organizations"  : organizations,
               "idOrganization" : idOrganization.id_Organization,
              }

    return render(request, 'peoples/people_info.html', context)



# Add new People
def addPeople(request):
    if request.method == 'POST':
        namePeople      = request.POST['namePeople']
        emailPeople     = request.POST['emailPeople']
        phonePeople     = request.POST['phonePeople']
        id_Organization = request.POST['id_Organization']

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

# Update people
def updatePeople(request, id_People):
    if request.method == 'POST':
        namePeople     = request.POST['namePeople']
        emailPeople    = request.POST['emailPeople']
        phonePeople    = request.POST['phonePeople']
        idOrganization = request.POST['orgPeople']

        people = models.TbPeople.objects.get(id_People = id_People)

        if people:

            if namePeople == people.namePeople and  emailPeople == people.emailPeople and phonePeople == people.phonePeople and idOrganization == people.id_Organization:
                organization       = models.TbOrganization.objects.get(id_Organization = idOrganization)
                people.namePeople  = namePeople
                people.emailPeople = emailPeople
                people.phonePeople = phonePeople
                people.id_Organization = organization
                people.save()
                messages.success( request, 'actualizado Correctamente' )
                return redirect('peopleInfo', id_People)

            else:
                messages.success( request, 'ingrese nuevos datos para actualizar' )
                return redirect('peopleInfo', id_People)
        else:
            messages.warning( request, 'ha ocurrido un error al actualizar')
            return redirect('peopleInfo', id_People)

#Delete people
def deletePeople(request, id_People):

    people = models.TbPeople.objects.get(id_People = id_People)
    if people:
        people = people.delete()
        messages.success( request, 'ha sido eliminado exitosamente')
        return redirect(to='peoples')
    else:
        messages.warning( request, 'ha ocurrido un error al eliminar')
        return redirect(to='peoples')

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

#----------------#
#     Devices    #
#----------------#

# show all devices
def devices(request):
    devices = models.Devices.objects.all()

    cpuDevices  = models.CpuDevices.objects.all()
    typeDevices = models.TypeDevices.objects.all()
    osDevices   = models.OsDevices.objects.all()
    zones       = models.Zones.objects.all()

    context = {'devices':devices, "cpuDevices":cpuDevices, "typeDevices":typeDevices, "osDevices":osDevices, "zones":zones }

    return render(request, 'devices/devices.html', context)

# add device
def add_device(request):

    ipDevice     = request.POST['ipDevice']
    nameDevice   = request.POST['nameDevice']
    creationDate = request.POST['creationDate']
    typeDevice   = request.POST['typeDevice']
    cpuDevice    = request.POST['cpuDevice']
    osDevice     = request.POST['osDevice']
    zone         = request.POST['zone']

    #foreignKeys
    idTypeDevice = models.TypeDevices.objects.get(idTypeDevice = typeDevice)
    idcpuDevice  = models.CpuDevices.objects.get(idCpuDevice = cpuDevice)
    idOsDevice   = models.OsDevices.objects.get(idOsDevice = osDevice)
    idZone       = models.Zones.objects.get(idZone = zone)

    device = models.Devices(ipDevice = ipDevice, nameDevice = nameDevice, creationDateDevice = creationDate,  typeDevices_idDevice = idTypeDevice, cpuDevices_idCpuDevice = idcpuDevice, osDevices_idOsDevice = idOsDevice, zones_idZone = idZone )
    device.save()

    return redirect('devices')

# Carga el formulario de actualización con los datos del dispositivo seleccionado
def formulario_actualizar_dispositivo(request, id_device):

    # Instancia del equipo seleccionado
    device  = models.tb_devices.objects.get(id_device = id_device)

    # Instancias de todos los cpu, so, zones, tipos disponibles
    cpus    = models.tb_cpu.objects.all()
    types   = models.tb_device_type.objects.all()
    so      = models.tb_os.objects.all()
    zones   = models.tb_zones.objects.all()

    # Instancia de los datos del equipo seleccionado
    cpu_    = models.tb_cpu.objects.get(cpu_name = device.id_cpu)
    so_     = models.tb_os.objects.get(os_name = device.id_os)

    zone_   = models.tb_zones.objects.get(zone_name = device.id_zone)
    device_ = models.tb_device_type.objects.get(id_device_type = str(device.id_device_type))

    # Fecha de creación en formato valido para Input Date HTML
    fecha = device.date_created.strftime('%Y-%m-%d')

    context = {"device": device, "cpus":cpus, "types":types, "os":so, "zones":zones, "fecha": fecha,
               "so_":so_.id_os, "zone_": zone_.id_zone, "cpu_":cpu_.id_cpu, "device_": device_.id_device_type}

    return render(request, 'dispositivos/actualizar_dispositivos.html', context)

# Actualizar la información del dispostivo seleccionado
def actualizar_dispositivo(request, id_device):

    # Instancia del dispositivo
    device = models.tb_devices.objects.get(id_device = id_device)

    #Asignación d elos nuevos valores
    device.ip_from          = request.POST['ip']
    device.date_created     = request.POST['fecha']
    device.id_device_type   = models.tb_device_type.objects.get(id_device_type = request.POST['type'])
    device.id_cpu           = models.tb_cpu.objects.get(id_cpu = request.POST['cpu'])
    device.id_os            = models.tb_os.objects.get(id_os = request.POST['os'])
    device.id_zone          = models.tb_zones.objects.get(id_zone = request.POST['zone'])

    # Guarda los cambios
    device.save()

    return redirect('/dispositivos/') 

# Eliminar dispostivos atravez de la interfaz
def delete_device(request, idDevice):


    device = models.Devices.objects.get(idDevice = idDevice)
    device.delete()

    return redirect('devices')

