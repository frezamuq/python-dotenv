from os.path import dirname, join

import sh
import dotenv

here = dirname(__file__)
dotenv_path = join(here, '.env')


def test_read_write():
    sh.touch(dotenv_path)
    success, key_to_set, value_to_set = dotenv.set_key(dotenv_path, 'HELLO', 'WORLD')
    stored_value = dotenv.get_key(dotenv_path, 'HELLO')
    assert stored_value == 'WORLD'
    sh.rm(dotenv_path)
