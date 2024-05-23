import os
from datetime import datetime
from io import BytesIO

from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.template.loader import get_template
from rest_framework.renderers import BaseRenderer
from xhtml2pdf import pisa

def get_customer_signature_img_path(instance, filename):
    return f'signatures/customer_{instance.id}/{filename}'


def get_file_attachment_path(instance, filename):
    return f'attachments/file_{instance.service_ticket_id}/{filename}'


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)


def dict_none_defaults(ctx):
    for k, v in ctx.items():
        if v is None or v == '':
            ctx[k] = '--'

    return ctx


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    s_url = settings.STATIC_URL
    s_root = settings.STATIC_ROOT
    m_url = settings.MEDIA_URL
    m_root = settings.MEDIA_ROOT

    if uri.startswith(m_url):
        pdf_path = os.path.join(m_root, uri.replace(m_url, ""))
    else:
        pdf_path = os.path.join(s_root, uri.replace(s_url, ""))
    return pdf_path


def render_to_pdf(template_src, context_dict={}):

    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(
        BytesIO(html.encode('UTF-8')),
        result,
        link_callback=link_callback
    )
    if not pdf.err:
        return result.getvalue()

    return None


class PDFRenderer(BaseRenderer):
    media_type = 'application/pdf'
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data
