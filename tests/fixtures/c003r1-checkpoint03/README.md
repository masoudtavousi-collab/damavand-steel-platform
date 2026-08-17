# C003-R1 Checkpoint 03 validation fixtures

The mutation manifest and adversarial schema/YAML fixtures test the versioned evidence extension only. They contain no Product, SKU, Availability, price, customer, order, payment, Runtime or Production population.

The canonical registry is the positive fixture. Tests deep-copy it in memory, so the exact 59-record source order and the immutable 115-record C003 base are not duplicated or edited.
