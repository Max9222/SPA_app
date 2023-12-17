from rest_framework.pagination import PageNumberPagination


class HabitsPagination(PageNumberPagination):
    """10 элементов на 1 странице, максимальное кол-во страниц - 100"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
