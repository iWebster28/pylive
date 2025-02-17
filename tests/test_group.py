""" Unit tests for PyLive """

import pytest
import time
import live

from tests.shared import open_test_set

def setup_module():
    # open_test_set()
    pass

@pytest.fixture(scope="module")
def group():
    set = live.Set()
    set.scan(scan_device=True)
    set.groups[0].stop()
    time.sleep(0.1)
    return set.groups[0]

def test_group_properties(group):
    assert group.group_index == 0
    assert group.track_index == 0
    assert len(group.tracks) == 2
    assert group.is_group

def test_group_get_clips(group):
    assert len(group.clips) == 256

def test_group_get_active_clips(group):
    assert len(group.active_clips) == 4

def test_group_stop(group):
    group.set.quantization = 0
    time.sleep(0.1)
    group.clips[0].play()
    time.sleep(0.2)
    assert group.is_playing
    group.stop()
    time.sleep(0.2)
    assert group.is_stopped
