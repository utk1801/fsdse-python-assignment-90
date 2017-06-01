from unittest import TestCase


class TestEqual_operator(TestCase):
    def test_equal_operator(self):
        from build import equal_operator

        import pandas as pd
        ds1 = pd.Series([2, 4, 6, 8, 10])
        ds2 = pd.Series([1, 3, 5, 7, 10])

        res = equal_operator(ds1, ds2)

        self.assertTrue([False, False, False, False, True], res.tolist())

    def test_greater_operator(self):
        from build import greater_than_operator

        import pandas as pd
        ds1 = pd.Series([2, 4, 6, 8, 10])
        ds2 = pd.Series([1, 3, 5, 7, 10])

        res = greater_than_operator(ds1, ds2)
        self.assertTrue([True, True, True, True, False], res.tolist())

    def test_less_operator(self):
        from build import less_than_operator

        import pandas as pd
        ds1 = pd.Series([2, 4, 6, 8, 10])
        ds2 = pd.Series([1, 3, 5, 7, 10])

        res = less_than_operator(ds1, ds2)

        self.assertTrue([False, False, False, False, False], res.tolist())
