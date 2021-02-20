import datetime
from unittest import TestCase

from whistler.whistlerAvailability import formDateFoundMessage


class TestFormDateFoundMessage(TestCase):
    def test_formDateFoundMessage(self):
        date1 = datetime.date(2021, 12, 1)
        msg = formDateFoundMessage([date1])
        self.assertIn('1-Dec', msg)

        date2 = datetime.date(2021, 11, 30)
        msg = formDateFoundMessage([date1, date2])
        self.assertIn('30-Nov', msg)
        self.assertIn('1-Dec', msg)

