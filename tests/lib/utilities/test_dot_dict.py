#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2017 Mozilla Corporation
#
# Contributors:
# Brandon Myers bmyers@mozilla.com


import pytest

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../lib"))
from utilities.dot_dict import DotDict

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
from unit_test_suite import UnitTestSuite


class TestDotDict(UnitTestSuite):
    def test_blank_init(self):
        dct = DotDict()
        assert dct.keys() == []

    def test_nonexisting_key(self):
        dct = DotDict()
        with pytest.raises(KeyError):
            dct.abcd

    def test_basic_init(self):
        dct = DotDict({'key1': 'value1', 'key2': 'value2'})
        assert sorted(dct.keys()) == sorted(['key1', 'key2'])
        assert dct.key1 == 'value1'
        assert dct.key2 == 'value2'

    def test_complex_init(self):
        original_dct = {
            'details': {
                'key1': 'value1'
            }
        }
        dct = DotDict(original_dct)
        assert dct.details == {'key1': 'value1'}
        assert dct.details.key1 == 'value1'
