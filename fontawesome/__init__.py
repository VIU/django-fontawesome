from django.conf import settings
try:
    from django.utils.html import format_html
except ImportError:
    # support django < 1.5. Taken from django.utils.html
    from django.utils import six
    def conditional_escape(text):
        """
        Similar to escape(), except that it doesn't operate on pre-escaped strings.
        """
        if isinstance(text, SafeData):
            return text
        else:
            return escape(text)

    def format_html(format_string, *args, **kwargs):
        """
        Similar to str.format, but passes all arguments through conditional_escape,
        and calls 'mark_safe' on the result. This function should be used instead
        of str.format or % interpolation to build up small HTML fragments.
        """
        args_safe = map(conditional_escape, args)
        kwargs_safe = dict([(k, conditional_escape(v)) for (k, v) in
                            six.iteritems(kwargs)])
        return mark_safe(format_string.format(*args_safe, **kwargs_safe))



class Icon(object):

    def __init__(self, id):
        self.id = id

    def as_html(self):
        if not self.id:
            return ''

        prefix = getattr(settings, 'FONTAWESOME_PREFIX', 'fa')
        return format_html('<i class="{0} {0}-{1}"></i>', prefix, self.id)

    def __str__(self):
        return self.id

    def __unicode__(self):
        return str(self)
