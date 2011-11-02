from webob.dec import wsgify
from webob import exc
from webob import Response
import urllib


class GetManifest(object):
    def __init__(self):
        pass

    @wsgify
    def __call__(self, req):
        url = req.params.get('url')
        if not url:
            raise exc.HTTPBadRequest('No url parameter')
        try:
            r = urllib.urlopen(url)
        except IOError, e:
            raise exc.HTTPBadGateway('Error getting url: %s' % e)
        if r.getcode() != 200:
            raise exc.HTTPBadGateway('URL returned error code: %s' \
                        % r.getcode())
        return Response(
            body=r.read(),
            content_type=r.headers.getheader('content-type'))


def main(global_conf, **settings):
    return GetManifest()
