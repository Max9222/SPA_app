from rest_framework.serializers import ValidationError


class NiceValidator:
    """Исключаем одновременный выбор связанной привычки, приятной привычки и указания вознаграждения."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        habit_reward = dict(value).get('reward')
        habit_is_nice = dict(value).get('nice')
        habit_is_pleasant = dict(value).get('pleasant_habit')

        if habit_is_nice and habit_reward is not None:
            raise ValidationError('Награды нет.')

        if habit_is_nice and habit_is_pleasant is not None:
            raise ValidationError('Исключено выбирать приятную и связанную привычки одновременно!')

        if habit_is_pleasant and habit_reward is None:
            raise ValidationError('Можно выбрать связанную привычку и награду одновременно!')


class TimeValidator:
    """Время выполнения должно быть не больше 120 секунд."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        complete_time = dict(value).get(self.field)
        if int(complete_time) > 120:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд!')


class IsNiceValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        nice_habit = dict(value).get(self.field)
        if nice_habit:
            if not nice_habit.nice:
                raise ValidationError('В связанные привычки могут попадать'
                                      ' только привычки с признаком приятной привычки!')


class PeriodValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if int(tmp_val) > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней!')
