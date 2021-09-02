from django import template
from django.utils.safestring import mark_safe

from core.models import Flowerinpot


register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'flower': {
        'История': 'history',
        'Строна': 'country',
        'Аромат': 'scent',
        'Состав': 'composition',
        'Размер': 'size'
    },
    'flowerinpot': {
        'История': 'history',
        'Строна': 'country',
        'Аромат': 'scent',
        'Состав': 'composition',
        'Размер': 'size',
        'Наличие поздрвительной карты': 'greeting_card',
        'Размер цветочного горшка': 'pot_size',
        'Цвет горшка': 'pot_color',
        'Инструкция по уходу': 'grooming_instructions'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Flowerinpot):
        if not product.greeting_card:
            PRODUCT_SPEC['flowerinpot'].pop('Размер цветочного горшка', None)
        else:
            PRODUCT_SPEC['flowerinpot']['Размер цветочного горшка'] = 'pot_size'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)

