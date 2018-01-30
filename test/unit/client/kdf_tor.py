"""
Unit tests for stem.client.kdf_tor.
"""

import unittest

import stem.client

KEY_1 = '\xec\xec.\xeb7R\xf2\n\xcb\xce\x97\xf4\x86\x82\x19#\x10\x0f\x08\xf0\xa2Z\xdeJ\x8f2\x8cc\xf6\xfa\x0e\t\x83f\xc5\xe2\xb3\x94\xa8\x13'
KEY_2 = '\xe0v\xe4\xfaTB\x91\x1c\x81Gz\xa0\tI\xcb{\xc56\xcfV\xc2\xa0\x19\x9c\x98\x9a\x06\x0e\xc5\xfa\xb0z\x83\xa6\x10\xf6r"<b'

DERIVED_1 = '\xca+\x81\x05\x14\x9d)o\xa6\x82\xe9B\xa8?\xf2\xaf\x85\x1b]6\xac\xcc\xbc\x91\xb1\xaf\xd7\xe0\xe9\x9dF#\xd8\xdbz\xe8\xe6\xca\x83,*\xe5scX\xbb+\xca \xcb\xa4\xbc\xad\x0f\x95\x0cO\xcc\xac\xf1\xc3\xbe\xc9\xe1\xf4\x90f\xdai\xf3\xf3\xf5\x14\xb5\xb9\x03U\xaf\x1e\x1b\xb1q||\x86A<_\xf7\xa0%\x86'
DERIVED_2 = '\xbc0\xf99\x8e;Te\xbb+\xdb\xabR3l\xb9f?\x07KZC8\xe7\xa15\xd1IS\xd9\xd4\x1e\x96\xf6\xcd\x82\x91\x0b}r\x7f\xc5\xc0\xb1/[\x97dW\xba\x82g\xe7m^\x06[\xe6\xf8\xb4\x83f>c\x8b\x0f\x03\xcc\x98\x1f~t\x88\xe1\x83\xec\xbf*_\x8cF\x0e1\xa9\x17\xce\xa6\xa3\xd1+]\x1f'


class TestKdfTor(unittest.TestCase):
  def test_kdf_tor(self):
    self.assertEqual(DERIVED_1, stem.client.kdf_tor(KEY_1))
    self.assertEqual(DERIVED_2, stem.client.kdf_tor(KEY_2))
