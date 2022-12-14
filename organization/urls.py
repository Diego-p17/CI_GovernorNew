from django.urls import path
from .           import views

urlpatterns = [
    # -- General -- #
    path('general/', views.get_general, name= "general"),
    # Country
    path('general/addCountry', views.addCountry, name= "addCountry"),
    path('general/deleteCountry/<int:id_Country>', views.deleteCountry, name= "deleteCountry"),
    path('general/updateCountry/<int:id_Country>', views.updateCountry, name= "updateCountry"),
    # City
    path('general/addCity', views.addCity, name= "addCity"),
    path('general/deleteCity/<int:id_City>', views.deleteCity, name= "deleteCity"),
    path('general/updateCity/<int:id_City>', views.updateCity, name= "updateCity"),
    #Os
    path('general/addOs', views.addOs, name= "addOs"),
    path('general/deleteOs/<int:id_Os>', views.deleteOs, name= "deleteOs"),
    path('general/updateOS/<int:id_Os>', views.updateOs, name= "updateOs"),
    #Platform
    path('general/addPlatform', views.addPlatform, name= "addPlatform"),
    path('general/deletePlatform/<int:id_Platform>', views.deletePlatform, name= "deletePlatform"),
    path('general/updatePlatform/<int:id_Platform>', views.updatePlatform, name= "updatePlatform"),
    #DeviceType
    path('general/addDeviceType', views.addDeviceType, name= "addDeviceType"),
    path('general/deleteDeviceType/<int:id_DeviceType>', views.deleteDeviceType, name= "deleteDeviceType"),
    path('general/updateDeviceType/<int:id_DeviceType>', views.updateDeviceType, name= "updateDeviceType"),
    #TokenType
    path('general/addTokenType', views.addTokenType, name= "addTokenType"),
    path('general/deleteTokenType/<int:id_TokenType>', views.deleteTokenType, name= "deleteTokenType"),
    path('general/updateTokenType/<int:id_TokenType>', views.updateTokenType, name= "updateTokenType"),
    #Settings type
    path('general/addSettingsType', views.addSettingsType, name= "addSettingsType"),
    path('general/deleteSettingsType/<int:id_SettingsType>', views.deleteSettingsType, name= "deleteSettingsType"),
    path('general/updateSettingsType/<int:id_SettingsType>', views.updateSettingsType, name= "updateSettingsType"),

    #################
    # Organizations #
    #################
    path('', views.getAllOrganizations, name= "home"),
    path('organization/<int:id_Organization>/', views.getOrganization, name = "organization"),
    path('addOrganization/', views.addOrganization, name = "addOrganization"),
    path('deleteOrganization/<int:id_Organization>', views.deleteOrganization, name = "deleteOrganization"),
    path('updateOrganization/<int:id_Organization>', views.updateOrganization, name = "updateOrganization"),

    #PeopleORG
    path('addPeopleOrg/<int:id_Organization>', views.addPeopleOrg, name = "addPeopleOrg"),
    path('deletePeopleOrg/<int:id_People>', views.deletePeopleOrg, name="deletePeopleOrg"),
    #SitesOrg
    path('addSiteOrg/<int:id_Organization>', views.addSiteOrg, name = "addSiteOrg"),
    path('deleteSiteOrg/<int:id_Site>', views.deleteSiteOrg, name = "deleteSiteOrg"),

    ###########
    #  Sites  #
    ###########
    path('sites/', views.getAllSites, name = "sites"),
    path('site/<int:id_Site>/', views.getSite, name = "site"),
    path('addSite/', views.addSite, name = "addSite"),
    path('updatesite/<int:id_Site>', views.updateSite, name = "updateSite"),
    #zoneSite
    path('addZone/<int:id_Site>/', views.addZone, name = "addZone"),
    path('updateZone/<int:id_Zone>/', views.updateZone, name = "updateZone"),
    path('deleteZone/<int:id_Zone>/', views.deleteZone, name = "deleteZone"),

    #############
    #  Peoples  #
    #############
    path('peoples/', views.getPeoples, name = "peoples"),
    path('people/<int:id_People>', views.peopleInfo, name = "people"),
    path('addPeople/', views.addPeople, name = "addPeople"),
    path('updatePeople/<int:id_People>/', views.updatePeople, name = "updatePeople"),
    path('deletePeople/<int:id_People>/', views.deletePeople, name = "deletePeople"),

    path('permisos_persona/<str:id_persona>/', views.permisos_persona, name = "permisos_persona"),
    path('eliminar_permiso/<str:id_persona>/<int:id_permiso>/', views.eliminar_permiso, name="eliminar_permiso"),
    path('modificar_permiso/<str:id_persona>/<int:id_permiso>/', views.modificar_permiso, name="modificar_permiso"),
    path('formulario_permisos/<str:id_persona>/', views.formulario_permisos, name = "formulario_permisos"),
    path('guardar_permiso/<str:id_persona>', views.guardar_permiso, name="guardar_permiso"),
    path('guardar_modificar_permiso/<str:id_persona>/<int:id_permiso>', views.guardar_modificar_permiso, name = "guardar_modificar_permiso"),


    ##################
    #  Dispositivos  #
    ##################
    path('devices/', views.getAllDevices, name = "devices"),
    path('device/<int:id_Device>', views.getDevice, name = "device"),
    path('addDevice/', views.addDevice, name = "addDevice"),
    path('updateDevice/<int:id_Device>/', views.updateDevice, name="updateDevice"),
    path('delete_device/<int:idDevice>/', views.delete_device, name = "delete_device"),
    path('addLocation/<int:id_Device>/', views.addLocation, name = "addLocation"),

    #####################
    #  Autporizathions  #
    #####################
    path('authorizations/', views.getAllAuthorizations, name = "authorizations"),


    #####################
    #    Aplications    #
    #####################
    path('aplications/', views.getAllAplications, name = "aplications"),
    path('aplication/<int:id_Aplication>', views.getAplication, name = "aplication"),
    path('addAplication/', views.addAplication, name = "addAplication"),
    path('addSubmodule/<int:id_Aplication>', views.addSubmodule, name = "addSubmodule"),
    path('updateSubModule/<int:id_SubModule>', views.updateSubModule, name = "updateSubModule"),
    path('deleteSubModule/<int:id_SubModule>', views.deleteSubModule, name = "deleteSubModule"),
]
