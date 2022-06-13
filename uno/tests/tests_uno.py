import logging
import unittest

from odoo.tests.common import BaseCase

_logger = logging.getLogger(__name__)

class TestUno(BaseCase):
    def test_fail(self):
        self.fail()
