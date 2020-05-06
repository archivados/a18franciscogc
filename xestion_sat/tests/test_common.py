# 1: imports of python lib

# 2: import of known third party lib

# 3:  imports of odoo
from odoo.tests.common import TransactionCase

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class TestCommonData(TransactionCase):
    """Common data for testing.
    """

    def setUp(self):
        super(TestCommonData, self).setUp()

        # Usefull models
        Partner = self.env['res.partner']
        Product = self.env['product.template']
        User = self.env['res.users'].with_context(no_reset_password=True)

        # Create a Users
        GroupUser = self.env.ref('xestion_sat.group_xestionsat_admin')

        self.test_admin_users = [
            # User 1
            User.create(
                {
                    'login': 'testusuario1',
                    'groups_id': [(6, 0, [GroupUser.id])],
                    'partner_id': self.env['res.partner'].create(
                        {
                            'name': 'María Técnica',
                            'email': 'a.m@example.com',
                        }
                    ).id
                }
            ),
            # User 2
            User.create(
                {
                    'login': 'testusuario2',
                    'groups_id': [(6, 0, [GroupUser.id])],
                    'partner_id': self.env['res.partner'].create(
                        {
                            'name': 'Laura Técnica',
                            'email': 'a.m@example.com',
                        }
                    ).id
                }
            ),
            # User 3
            User.create(
                {
                    'login': 'testusuario3',
                    'partner_id': self.env['res.partner'].create(
                        {
                            'name': 'Juan',
                            'email': 'a.m@example.com',
                        }
                    ).id
                }
            ),
        ]

        # Company 1 addresses
        partner1_addresses = [
            Partner.create(
                {
                    'name': 'Oficina A',
                    'street': 'Rúa A, número 3',
                    'type': 'other',
                    'city': 'Santiago de Compostela',
                    'parent_id': self.partner_1.id,
                }
            ),
            Partner.create(
                {
                    'name': 'Oficina B',
                    'type': 'other',
                    'street': 'Rúa B, número 34',
                    'city': 'Santiago de Compostela',
                    'parent_id': self.partner_1.id,
                }
            ),
        ]

        # Company 1 employees
        partner1_employees = [
            Partner.create(
                {
                    'name': 'Argentina',
                    'type': 'contact',
                    'parent_id': self.partner_1.id,
                }
            ),
            Partner.create(
                {
                    'name': 'Roberto',
                    'type': 'contact',
                    'parent_id': self.partner_1.id,
                }
            ),
        ]

        # Company 2 addresses
        partner2_addresses = [
            Partner.create(
                {
                    'name': 'Oficina Z',
                    'street': 'Rúa Z, número 12',
                    'city': 'Santiago de Compostela',
                    'parent_id': self.partner_2.id,
                }
            ),
            Partner.create(
                {
                    'name': 'Oficina Y',
                    'street': 'Rúa Y, número 1',
                    'city': 'Santiago de Compostela',
                    'parent_id': self.partner_2.id,
                }
            ),
        ]

        # Company 2 employees
        partner2_employees = [
            Partner.create(
                {
                    'name': 'Jesús',
                    'type': 'contact',
                    'parent_id': self.partner_2.id,
                }
            ),
            Partner.create(
                {
                    'name': 'Miguel',
                    'type': 'contact',
                    'parent_id': self.partner_2.id,
                }
            ),
        ]

        # Create a Customers
        self.partners = [
            # Company 1
            (
                Partner.create(
                    {
                        'name': 'Empresa ABC',
                        'is_company': True,
                    }
                ),
                {
                    'addresses': partner1_addresses,
                    'employees': partner1_employees,
                }
            ),
            # Company 2
            (
                Partner.create(
                    {
                        'name': 'Empresa ZYX',
                        'is_company': True,
                    }
                ),
                {
                    'addresses': partner2_addresses,
                    'employees': partner2_employees,
                }
            ),
        ]

        # Create Product for Devices Components
        self.products = [
            # Product_1
            Product.create(
                {
                    'name': 'CPU',
                    'type': 'consu',
                }
            ),
            # Product_2
            Product.create(
                {
                    'name': 'RAM',
                    'type': 'consu',
                }
            ),
            # Product_3
            Product.create(
                {
                    'name': 'Disco duro',
                    'type': 'consu',
                }
            ),
            # Product_4
            Product.create(
                {
                    'name': 'Tarxeta gráfica',
                    'type': 'consu',
                }
            ),
        ]

        # Create Product for Incidence Atcions
        self.incidence_actions = [
            # Action_1
            Product.create(
                {
                    'name': 'Limpeza de virus',
                    'type': 'sat',
                }
            ),
            # Action_2
            Product.create(
                {
                    'name': 'Formateo con GNU/Linux',
                    'type': 'sat',
                }
            ),
        ]
