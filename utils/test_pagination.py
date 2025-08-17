from unittest import TestCase
from utils.pagination import make_pagination_range, make_pagination
from types import SimpleNamespace



class PaginationTest(TestCase):
    def test_make_pagination_range_retunrs_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa: E501
        #  Current Pages = 1 Qty Pages = 2 Middle Page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            #  Current Pages = 2 Qty Pages = 2 Middle Page = 2
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            #  Current Pages = 3 Qty Pages = 2 Middle Page = 2
            #  HERE RANGE SHOULD CHANGE
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)

        pagination = make_pagination_range(
            #  Current Pages = 4 Qty Pages = 2 Middle Page = 2
            #  HERE RANGE SHOULD CHANGE
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=4,
        )['pagination']
        self.assertEqual([3, 4, 5, 6], pagination)
    
    def test_make_sure_middle_ranges_are_correct(self): 
        pagination = make_pagination_range(
            #  Current Pages = 10 Qty Pages = 2 Middle Page = 2
            #  HERE RANGE SHOULD CHANGE
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=10,
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)

        pagination = make_pagination_range(
            #  Current Pages = 12 Qty Pages = 2 Middle Page = 2
            #  HERE RANGE SHOULD CHANGE
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=12,
        )['pagination']
        self.assertEqual([11, 12, 13, 14], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination = make_pagination_range(
            #  Current Pages = 18 Qty Pages = 2 Middle Page = 2
            #  HERE RANGE SHOULD CHANGE
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=18,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = make_pagination_range(
            #  Current Pages = 19 Qty Pages = 2 Middle Page = 2
            #  HERE RANGE SHOULD CHANGE
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=19,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = make_pagination_range(
            #  Current Pages = 20 Qty Pages = 2 Middle Page = 2
            #  HERE RANGE SHOULD CHANGE
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=20,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = make_pagination_range(
            #  Current Pages = 21 Qty Pages = 2 Middle Page = 2
            #  HERE RANGE SHOULD CHANGE
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=21,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

    def test_make_pagination_exption_error(self):
        queryset = list(range(20))
        par_page = 10

        request = SimpleNamespace(GET={'page': 'abclo'})

        page_obj, _ = make_pagination(request, queryset, par_page, qty_pages=4)

        self.assertEqual(page_obj.number, 1)
        
    

