from django.db import IntegrityError

from foo.bar.models import Bar

class IntegrityTest(TestCase):

    def test_integrity(self):
        bar = Bar()
        self.assertRaises(IntegrityError, bar.save)
