#hexmap_builder_test.py

import hexmap_builder
def test_hexmap(sample_size=10000):
    for i in range(sample_size):
        hexmap_builder.print_hex()
        hexmap_builder.rnp_settlement()
        hexmap_builder.print_fae_hex()
        hexmap_builder.hex()
        hexmap_builder.hex(argv=["-f"])
        hexmap_builder.hex(argv=["-s"])

test_hexmap()