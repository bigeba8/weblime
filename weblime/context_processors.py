from django.http import HttpRequest


def seo_attrs(request: HttpRequest):
    """returns seo attributes to be merged into the context

    Arguments:
        request {HttpRequest} -- request object
    """
    return {
        'seo_title': 'WebLime',
        'seo_description': 'A Website Design & Digital Marketing Agency with experience in building results-driven custom web-based solutions. Our highly trained staff of web and marketing professionals are eager to work on your next digital project.'
    }
