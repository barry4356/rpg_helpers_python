#hexmap_builder_test.py

import hexmap_builder
def test_hexmap(sample_size=100000):
    for i in range(sample_size):
        hexmap_builder.print_hex()
        hexmap_builder.rnp_settlement()
        hexmap_builder.print_fae_hex()

test_hexmap()