from odoo.tests.common import TransactionCase


class TestCommonData(TransactionCase):
    '''Test.
    '''

    def setUp(self):
        super(TestCommonData, self).setUp()

        # Usefull models
        Partner = self.env['res.partner']
        Product = self.env['product.template']
        User = self.env['res.users'].with_context(no_reset_password=True)

        # Create a Users
        group_user = self.env.ref('xestion_sat.group_xestionsat_admin')

        # User 1
        self.test_admin_1 = User.create(
            {
                'name': 'María Técnica',
                'login': 'testusuario1',
                'email': 'a.m@example.com',
                'groups_id': [(6, 0, [group_user.id])],
            }
        )
        # User 2
        self.test_admin_2 = User.create(
            {
                'name': 'Laura Técnica',
                'login': 'testusuario2',
                'email': 'a.m@example.com',
                'groups_id': [(6, 0, [group_user.id])],
            }
        )
        # User 3
        self.test_noadmin_1 = User.create(
            {
                'name': 'Juan',
                'login': 'testusuario3',
                'email': 'a.m@example.com',
            }
        )

        # Create a Customers
        # Company 1
        self.partner_1 = Partner.create(
            {
                'create_uid': self.test_admin_1.id,
                'name': 'Empresa ABC',
                'is_company': True,
            }
        )

        # Company 1 addresses
        self.partner_1_address_1 = Partner.create(
            {
                'name': 'Oficina A',
                'street': 'Rúa A, número 3',
                'type': 'other',
                'city': 'Santiago de Compostela',
                'parent_id': self.partner_1.id,
            }
        )
        self.partner_1_address_2 = Partner.create(
            {
                'name': 'Oficina B',
                'type': 'other',
                'street': 'Rúa B, número 34',
                'city': 'Santiago de Compostela',
                'parent_id': self.partner_1.id,
            }
        )
        # Company 1 employees
        self.partner_1_employee_1 = Partner.create(
            {
                'name': 'Argentina',
                'type': 'contact',
                'parent_id': self.partner_1.id,
            }
        )
        self.partner_1_employee_2 = Partner.create(
            {
                'name': 'Roberto',
                'type': 'contact',
                'parent_id': self.partner_1.id,
            }
        )

        # Company 2
        self.partner_2 = Partner.create(
            {
                'name': 'Empresa ZYX',
                'is_company': True,
            }
        )
        # Company 2 addresses
        self.partner_2_address_1 = Partner.create(
            {
                'name': 'Oficina Z',
                'street': 'Rúa Z, número 12',
                'city': 'Santiago de Compostela',
                'parent_id': self.partner_2.id,
            }
        )
        self.partner_2_address_2 = Partner.create(
            {
                'name': 'Oficina Y',
                'street': 'Rúa Y, número 1',
                'city': 'Santiago de Compostela',
                'parent_id': self.partner_2.id,
            }
        )
        # Company 2 employees
        self.partner_2_employee_1 = Partner.create(
            {
                'name': 'Jesús',
                'type': 'contact',
                'parent_id': self.partner_2.id,
            }
        )
        self.partner_2_employee_2 = Partner.create(
            {
                'name': 'Miguel',
                'type': 'contact',
                'parent_id': self.partner_2.id,
            }
        )

        # Create a Devices Components
        # Device Component 1 (Product)
        self.product_1 = Product.create(
            {
                'name': 'CPU',
                'type': 'consu',
            }
        )

        # Device Component 2 (Product)
        self.product_1 = Product.create(
            {
                'name': 'RAM',
                'type': 'consu',
            }
        )

        # Device Component 3 (Product)
        self.product_1 = Product.create(
            {
                'name': 'Disco duro',
                'type': 'consu',
            }
        )

        # Device Component 4 (Product)
        self.product_1 = Product.create(
            {
                'name': 'Tarxeta gráfica',
                'type': 'consu',
            }
        )
