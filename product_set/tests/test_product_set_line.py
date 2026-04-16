# Copyright 2024 Camptocamp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo.tests.common import TransactionCase


class TestProductSetLine(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.uom_unit = cls.env.ref("uom.product_uom_unit")
        cls.uom_dozen = cls.env.ref("uom.product_uom_dozen")
        product = cls.env["product.product"].create({"name": "Test Product"})
        product_set = cls.env["product.set"].create({"name": "Test Set"})
        cls.line = cls.env["product.set.line"].create(
            {
                "product_set_id": product_set.id,
                "product_id": product.id,
                "quantity": 1,
            }
        )

    def test_uom_id_can_be_set(self):
        line = self.line
        line.uom_id = self.uom_unit
        self.assertEqual(line.uom_id, self.uom_unit)

    def test_uom_id_can_be_changed(self):
        line = self.line
        line.uom_id = self.uom_unit
        line.uom_id = self.uom_dozen
        self.assertEqual(line.uom_id, self.uom_dozen)

    def test_uom_id_is_optional(self):
        line = self.line
        line.uom_id = False
        self.assertFalse(line.uom_id)
