# 1: imports of python lib
from datetime import datetime

# 2: import of known third party lib

# 3:  imports of odoo
from .test_common import TestCommonData
from odoo.exceptions import ValidationError

# 4:  imports from odoo modules

# 5: local imports

# 6: Import of unknown third party lib


class XestionsatTest(TestCommonData):
    """Model tests of the xestiónSAT module.
    """

    def setUp(self):
        super(XestionsatTest, self).setUp()
        self.Device = self.env['xestionsat.device']
        self.DeviceComponent = self.env['xestionsat.device.component']
        self.Incidence = self.env['xestionsat.incidence']
        self.IncidenceState = self.env['xestionsat.incidence.state']
        self.IncidencePlace = self.env['xestionsat.incidence.assistance_place']

        # Create Devices Components
        # Device Component 1 (Product)
        self.componet_1 = self.DeviceComponent.create(
            {
                # Required fields
                'template_id': self.product_1.id,
                # Optional fields
                'serial': '1111',
                'observation': 'Unha observación',
                'date_registration': datetime.now().strftime('%Y-%m-%d'),
                # 'date_cancellation': '',
            }
        )
        # Device Component 2 (Product)
        self.componet_2 = self.DeviceComponent.create(
            {
                # Required fields
                'template_id': self.product_2.id,
                # Optional fields
                'serial': '2222',
                'observation': 'Unha observación',
                'date_registration': datetime.now().strftime('%Y-%m-%d'),
                # 'date_cancellation': '',
            }
        )
        # Device Component 3 (Product)
        self.componet_3 = self.DeviceComponent.create(
            {
                # Required fields
                'template_id': self.product_3.id,
                # Optional fields
                'serial': '3333',
                'observation': 'Unha observación',
                'date_registration': datetime.now().strftime('%Y-%m-%d'),
                # 'date_cancellation': '',
            }
        )
        # Device Component 4 (Product)
        self.componet_4 = self.DeviceComponent.create(
            {
                # Required fields
                'template_id': self.product_4.id,
                # Optional fields
                'serial': '4444',
                'observation': 'Unha observación',
                'date_registration': datetime.now().strftime('%Y-%m-%d'),
                # 'date_cancellation': '',
            }
        )

        # Create Incidence States
        # Incidence State 1
        self.incidence_state_1 = self.IncidenceState.create(
            {
                # Required fields
                'state': 'Pending',
                'sequence': 1,
                # Optional fields
                'description': 'Work without starting',
            }
        )
        # Incidence State 2
        self.incidence_state_2 = self.IncidenceState.create(
            {
                # Required fields
                'state': 'Started',
                'sequence': 2,
                # Optional fields
                'description': 'Work in progress',
            }
        )

        # Create Incidence Assistance Place
        # Incidence Assistance Place 1
        self.incidence_place_1 = self.IncidencePlace.create(
            {
                # Required fields
                'assistance_place': 'In workshop',
                'description': 'In our workshop',
            }
        )
        # Incidence Assistance Place 2
        self.incidence_place_2 = self.IncidencePlace.create(
            {
                # Required fields
                'assistance_place': 'On-site',
                'description': 'At the Customers workplace',
            }
        )

    def test_create_device(self):
        """Device model test.
        """
        users_list = [
            self.partner_1_employee_1.id,
        ]

        componets_list = [
            self.componet_1.id,
            self.componet_2.id,
            self.componet_4.id,
        ]

        # Device 1
        self.device_1 = self.Device.sudo(self.test_admin_1).create(
            {
                # Required fields
                'created_by_id': self.test_admin_1.id,
                'owner_id': self.partner_1.id,
                'headquarter_id': self.partner_1_address_2.id,
                'name': 'Equipo 1',
                'state': 'operational',

                # Optional fields
                'user_ids': [(6, 0, users_list)],
                'devicecomponents_ids': [(6, 0, componets_list)],
                'internal_id': '20-000001',
                'location': 'Sala de reunións grande',
                'description': 'Equipo para presentacións',
                'observation': 'Saídas de video: 2xHDMI, 1xDVI e 1xVGA',
                'date_registration': datetime.now().strftime('%Y-%m-%d'),
                # 'date_cancellation': '',
            }
        )

        # Check that device is created or not
        assert self.device_1, "Device not created"

        # User assignment checks
        # Add device user
        len_user_ids = len(self.device_1['user_ids'])

        self.device_1['user_ids'] = [(4, self.partner_1_employee_2.id)]
        self.assertEqual(
            len(self.device_1['user_ids']),
            len_user_ids + 1,
            msg='\nAdd Device User ERRO: '
            + '\n Device: ' + self.device_1.name
            + '\n len(user_ids): ' + str(len_user_ids)
        )
        # Remove device user
        len_user_ids = len(self.device_1['user_ids'])

        self.device_1['user_ids'] = [(2, self.partner_1_employee_1.id)]
        self.assertEqual(
            len(self.device_1['user_ids']),
            len_user_ids - 1,
            msg='\nRemove Device User ERRO: '
            + '\n Device: ' + self.device_1.name
            + '\n len(user_ids): ' + str(len_user_ids)
        )

        # Components assignment checks
        # Add device component
        len_devicecomponents_ids = len(self.device_1['devicecomponents_ids'])

        self.device_1['devicecomponents_ids'] = [(4, self.componet_3.id)]
        self.assertEqual(
            len(self.device_1['devicecomponents_ids']),
            len_devicecomponents_ids + 1,
            msg='\nAdd Componet ERRO:'
            + '\n Product: ' + self.device_1.name
            + '\n len(len_devicecomponents_ids): '
                + str(len_devicecomponents_ids)
        )
        # Remove device component
        len_devicecomponents_ids = len(self.device_1['devicecomponents_ids'])

        self.device_1['devicecomponents_ids'] = [(2, self.componet_3.id)]
        self.assertEqual(
            len(self.device_1['devicecomponents_ids']),
            len_devicecomponents_ids - 1,
            msg='\nRemove Componet ERRO:'
            + '\n Product: ' + self.device_1.name
            + '\n len(len_devicecomponents_ids): '
                + str(len_devicecomponents_ids)
        )
        len_user_ids = len(self.device_1['devicecomponents_ids'])

        # Check constraints
        # Check Odoo user constraint
        with self.assertRaises(ValidationError):
            self.device_1.created_by_id = self.test_admin_2

        # Check headquarters constraints
        with self.assertRaises(ValidationError):
            self.device_1.headquarter_id = self.partner_2_address_2

        # Check device user constraint
        with self.assertRaises(ValidationError):
            self.device_1['user_ids'] = (4, self.partner_2_employee_2.id)

        return self.device_1

    def test_create_incidence(self):
        """Incidence model test.
        """
        device_1 = self.test_create_device()

        # Incidence 1
        self.incidence_1 = self.Incidence.sudo(self.test_admin_1).create(
            {
                # Required fields
                'created_by_id': self.test_admin_1.id,
                'customer_id': device_1['owner_id'].id,
                # 'device_ids': self.partner_1.id,
                'title': 'Incidencia 1: ' + device_1.name,
                'failure_description': 'Non se conecta a internet',
                'state': self.incidence_state_1.id,

                # Optional fields
                'observation': 'Unha observación',
                'assistance_place': self.incidence_place_1.id,
                # 'incidence_action_ids': ,
                'date_start': datetime.now().strftime('%Y-%m-%d'),
                # 'date_end': '',
            }
        )

        # Check that device is created or not
        assert self.incidence_1, "Device not created"

        # Check constraints
        # Check Odoo user constraint
        with self.assertRaises(ValidationError):
            self.incidence_1.created_by_id = self.test_admin_2
