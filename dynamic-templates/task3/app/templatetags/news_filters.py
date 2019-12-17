from django import template
from datetime import datetime, timedelta

register = template.Library()


@register.filter
def format_date(value: float):
    now = datetime.now()
    datetime_value = datetime.fromtimestamp(value)
    less_10_minutes = timedelta(minutes=10)
    less_24_hours = timedelta(hours=24)
    delta = now - datetime_value
    if delta <= less_10_minutes:
        return 'только что'
    elif delta <= less_24_hours:
        hours = round((delta.seconds / 60) / 60)
        return f'{hours} часов назад'
    else:
        return datetime.strftime(datetime_value, '%Y-%m-%d')


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value: int):
    if value < -5:
        return 'все плохо'
    elif -5 <= value < 5:
        return 'нейтрально'
    elif value >= 5:
        return 'хорошо'
    else:
        return value


@register.filter
def format_num_comments(value: int):
    if value == 0:
        return 'Оставьте комментарий'
    elif 0 < value <= 50:
        return value
    else:
        return '50+'


@register.filter
def format_selftext(value: str, count: int = None):
    if count is not None:
        post_text = value.split()
        first_part_text = post_text[:count]
        first_part_text.append('...')
        new_post_text = first_part_text + post_text[-count:]
        new_post_text = ' '.join(new_post_text)
        return new_post_text
    else:
        return value
