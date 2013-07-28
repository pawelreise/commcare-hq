from django.utils.unittest.case import TestCase
from corehq.apps.app_manager.models import Application
from corehq.apps.app_manager.tests.util import TestFileMixin


# snippet from http://stackoverflow.com/questions/321795/comparing-xml-in-a-unit-test-in-python/7060342#7060342
from doctest import Example
from lxml.doctestcompare import LXMLOutputChecker


class XmlTest(TestCase):

    def assertXmlEqual(self, want, got):
        checker = LXMLOutputChecker()
        if not checker.check_output(want, got, 0):
            message = checker.output_difference(Example("", want), got, 0)
            raise AssertionError(message)
# end snippet


class SuiteTest(XmlTest, TestFileMixin):
    file_path = ('data', 'suite')

    def test_normal_suite(self):
        app = Application.wrap(self.get_json('app'))
        self.assertXmlEqual(self.get_xml('normal-suite'), app.create_suite())

    def test_tiered_select(self):
        app = Application.wrap(self.get_json('tiered-select'))
        self.assertXmlEqual(self.get_xml('tiered-select'), app.create_suite())
