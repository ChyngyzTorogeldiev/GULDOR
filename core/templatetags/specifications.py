from django import template
from django.utils.safestring import mark_safe

from core.models import Flowerinpot, Flower, WeddingFlower, OtherFlower


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
        'Количество роз в букете': 'quantity',
        'Длина букета: (см)': 'size',
        'Наличие поздрвительной карты': 'greeting_card',
    },
    'flowerinpot': {
       
        'Высота цветов с учетом горшка: (см)': 'size',
        'Наличие поздрвительной карты': 'greeting_card',
        'Размер цветочного горшка: (см)': 'pot_size',
        'Цвет горшка': 'pot_color',
        'Инструкция по уходу': 'grooming_instructions'
    },
    'weddingflower': {
        'Длина букета: (см)': 'size',
        'Наличие бутоньерки': 'butonniere'
    },
    'otherflower': {
        'Длина букета: (см)': 'size',
        'Наличие поздрвительной карты': 'greeting_card',
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
            PRODUCT_SPEC['flowerinpot'].pop('Размер цветочного горшка: (см)', None)
        else:
            PRODUCT_SPEC['flowerinpot']['Размер цветочного горшка: (см)'] = 'pot_size'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)

