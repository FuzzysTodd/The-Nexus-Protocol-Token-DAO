from geopy.geocoders.algolia import AlgoliaPlaces as AlgoliaPlaces
from geopy.geocoders.arcgis import ArcGIS as ArcGIS
from geopy.geocoders.azure import AzureMaps as AzureMaps
from geopy.geocoders.baidu import Baidu as Baidu, BaiduV3 as BaiduV3
from geopy.geocoders.banfrance import BANFrance as BANFrance
from geopy.geocoders.base import options as options
from geopy.geocoders.bing import Bing as Bing
from geopy.geocoders.databc import DataBC as DataBC
from geopy.geocoders.geocodeearth import GeocodeEarth as GeocodeEarth
from geopy.geocoders.geocodio import Geocodio as Geocodio
from geopy.geocoders.geolake import Geolake as Geolake
from geopy.geocoders.geonames import GeoNames as GeoNames
from geopy.geocoders.google import GoogleV3 as GoogleV3
from geopy.geocoders.here import Here as Here, HereV7 as HereV7
from geopy.geocoders.ignfrance import IGNFrance as IGNFrance
from geopy.geocoders.mapbox import MapBox as MapBox
from geopy.geocoders.mapquest import MapQuest as MapQuest
from geopy.geocoders.maptiler import MapTiler as MapTiler
from geopy.geocoders.nominatim import Nominatim as Nominatim
from geopy.geocoders.opencage import OpenCage as OpenCage
from geopy.geocoders.openmapquest import OpenMapQuest as OpenMapQuest
from geopy.geocoders.pelias import Pelias as Pelias
from geopy.geocoders.photon import Photon as Photon
from geopy.geocoders.pickpoint import PickPoint as PickPoint
from geopy.geocoders.smartystreets import LiveAddress as LiveAddress
from geopy.geocoders.tomtom import TomTom as TomTom
from geopy.geocoders.what3words import What3Words as What3Words, What3WordsV3 as What3WordsV3
from geopy.geocoders.yandex import Yandex as Yandex

__all__ = ['get_geocoder_for_service', 'options', 'AlgoliaPlaces', 'ArcGIS', 'AzureMaps', 'Baidu', 'BaiduV3', 'BANFrance', 'Bing', 'DataBC', 'GeocodeEarth', 'Geocodio', 'GeoNames', 'GoogleV3', 'Geolake', 'Here', 'HereV7', 'IGNFrance', 'MapBox', 'MapQuest', 'MapTiler', 'Nominatim', 'OpenCage', 'OpenMapQuest', 'PickPoint', 'Pelias', 'Photon', 'LiveAddress', 'TomTom', 'What3Words', 'What3WordsV3', 'Yandex']

def get_geocoder_for_service(service):
    '''
    For the service provided, try to return a geocoder class.

    >>> from geopy.geocoders import get_geocoder_for_service
    >>> get_geocoder_for_service("nominatim")
    geopy.geocoders.nominatim.Nominatim

    If the string given is not recognized, a
    :class:`geopy.exc.GeocoderNotFound` exception is raised.

    Given that almost all of the geocoders provide the ``geocode``
    method it could be used to make basic queries based entirely
    on user input::

        from geopy.geocoders import get_geocoder_for_service

        def geocode(geocoder, config, query):
            cls = get_geocoder_for_service(geocoder)
            geolocator = cls(**config)
            location = geolocator.geocode(query)
            return location.address

        >>> geocode("nominatim", dict(user_agent="specify_your_app_name_here"), "london")
        \'London, Greater London, England, SW1A 2DX, United Kingdom\'
        >>> geocode("photon", dict(), "london")
        \'London, SW1A 2DX, London, England, United Kingdom\'

    '''
