# -*- coding: utf-8 -*-

MEDIA_ROOT = "/var/Projects/ruspaket_media/media"
STATIC_ROOT = "/var/Projects/ruspaket_media/static"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

TEMPLATE_DEBUG = False
THUMBNAIL_DEBUG = False