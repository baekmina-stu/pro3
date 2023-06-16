from django import template
import re
from django.utils.html import conditional_escape


register = template.Library()

@register.filter
def process_html(value):
    # HTML 코드를 처리하여 변환하는 로직을 구현합니다
    processed_html = re.sub(
        r'<font\s+color="(.*?)"\s+style="background-color:\s+rgb\((\d+),\s+(\d+),\s+(\d+)\);">',
        r'<span style="color: \1; background-color: rgb(\2, \3, \4);">',
        value
    )
    return conditional_escape(processed_html)

