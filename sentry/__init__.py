"""
Sentry
~~~~~~
"""
# pkg_resources spits out annoying "Module x was already imported ..." UserWarning
# so we're setting the VERSION manually
VERSION = '1.6.1'
# try:
#     VERSION = __import__('pkg_resources') \
#         .get_distribution('django-sentry').version
# except Exception, e:
#     VERSION = 'unknown'