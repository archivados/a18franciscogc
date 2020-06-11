# 1: imports of python lib
from datetime import datetime, timedelta

# 2: import of known third party lib

# 3:  imports of odoo
from odoo.exceptions import ValidationError

# 4:  imports from odoo modules
from .test_common import TestCommonData
from ..models.xestionsat_common import STATE_DEVICE

# 5: local imports

# 6: Import of unknown third party lib


class XestionsatTest(TestCommonData):
    """Model tests of the xestiónSAT module.
    """
    # Constants
    LIST_ADD_ALL = 6
    LIST_ADD = 4
    LIST_REMOVE = 3

    def setUp(self):
        super(XestionsatTest, self).setUp()
        self.Device = self.env['xestionsat.device']
        self.DeviceComponent = self.env['xestionsat.device.component']
        self.Incidence = self.env['xestionsat.incidence']
        self.IncidenceStage = self.env['xestionsat.incidence.stage']
        self.IncidencePlace = self.env['xestionsat.incidence.assistance_place']

        # Create Devices Components
        # Device Component 1 (Product)
        self.componets = [
            self.create_device_componet(self.products[0], '1111'),
            self.create_device_componet(self.products[1], '2222'),
            self.create_device_componet(self.products[2], '3333'),
            self.create_device_componet(self.products[3], '4444'),
        ]

        # Create Incidence Stages
        self.incidence_stages = [
            # Incidence Stage 1
            self.IncidenceStage.create(
                {
                    # Required fields
                    'stage': 'Pending',
                    'sequence': 11,
                    # Optional fields
                    'description': 'Work without starting',
                }
            ),
            # Incidence Stage 2
            self.IncidenceStage.create(
                {
                    # Required fields
                    'stage': 'Started',
                    'sequence': 22,
                    # Optional fields
                    'description': 'Work in progress',
                }
            ),
        ]

        # Create Incidence Assistance Place
        self.incidence_places = [
            # Incidence Assistance Place 1
            self.IncidencePlace.create(
                {
                    # Required fields
                    'assistance_place': 'In workshop',
                    'description': 'In our workshop',
                }
            ),
            # Incidence Assistance Place 2
            self.IncidencePlace.create(
                {
                    # Required fields
                    'assistance_place': 'On-site',
                    'description': 'At the Customers workplace',
                }
            ),
        ]

    def test_create_device(self):
        """Device model test.
        """
        # Data for checks
        users_list = [
            self.partner0_employees[0].id,
        ]

        componets_list = [
            self.componets[0].id,
            self.componets[1].id,
            self.componets[3].id,
        ]

        internal_id = '20-000001'
        location = 'Sala de reunións grande'
        description = 'Equipo para presentacións'
        observation = 'Saídas de video: 2xHDMI, 1xDVI e 1xVGA'
        date_cancellation = (datetime.now() + timedelta(days=(10))) \
            .strftime('%Y-%m-%d')

        # Device 1
        device_1 = self.create_device(
            'Equipo1_incidencia',
            self.test_admin_users[0],
            self.partners[0],
            self.partner0_addresses[0],
        )

        # Check that device is created or not
        assert device_1, "Device not created"

        # Optional fields assignment checks
        device_1.internal_id = internal_id
        self.assertEqual(
            device_1.internal_id,
            internal_id,
            msg='Add internal_id'
        )
        device_1.location = location
        self.assertEqual(
            device_1.location,
            location,
            msg='Add location'
        )
        device_1.description = description
        self.assertEqual(
            device_1.description,
            description,
            msg='Add description'
        )
        device_1.observation = observation
        self.assertEqual(
            device_1.observation,
            observation,
            msg='Add observation'
        )
        device_1.date_cancellation = date_cancellation
        self.assertEqual(
            device_1.date_cancellation.strftime('%Y-%m-%d'),
            date_cancellation,
            msg='Add date_cancellation'
        )

        # User assignment checks
        # Add users list
        device_1.user_ids = [
            (self.LIST_ADD_ALL, 0, users_list)]
        self.assertEqual(
            len(device_1.user_ids),
            len(users_list),
            msg='\nAdd Device User: '
            + '\n Device: ' + device_1.name
            + '\n len(device_1.user_ids): ' + str(len(device_1.user_ids))
            + '\n len(users_ids): ' + str(len(users_list))
        )

        # Add device user
        len_user_ids = len(device_1.user_ids)

        device_1.user_ids = [
            (self.LIST_ADD, self.partner0_employees[1].id)]
        self.assertEqual(
            len(device_1.user_ids),
            len_user_ids + 1,
            msg='\nAdd Device User: '
            + '\n Device: ' + device_1.name
            + '\n len(device_1.user_ids): ' + str(len(device_1.user_ids))
            + '\n len(user_ids): ' + str(len_user_ids)
        )
        # Remove device user
        len_user_ids = len(device_1.user_ids)

        device_1.user_ids = [
            (self.LIST_REMOVE, self.partner0_employees[0].id)]
        self.assertEqual(
            len(device_1.user_ids),
            len_user_ids - 1,
            msg='\nRemove Device User: '
            + '\n Device: ' + device_1.name
            + '\n len(device_1.user_ids): ' + str(len(device_1.user_ids))
            + '\n len(user_ids): ' + str(len_user_ids)
        )

        # Components assignment checks
        # Add device component list
        device_1.devicecomponent_ids = [
            (self.LIST_ADD_ALL, 0, componets_list)]
        self.assertEqual(
            len(device_1.devicecomponent_ids),
            len(componets_list),
            msg='\nAdd Componet: '
            + '\n Device: ' + device_1.name
            + '\n len(device_1.user_ids): '
                + str(len(device_1.devicecomponent_ids))
            + '\n len(componets_list): '
                + str(componets_list)
        )
        # Add device component
        len_devicecomponent_ids = len(device_1.devicecomponent_ids)

        device_1.devicecomponent_ids = [
            (self.LIST_ADD, self.componets[2].id)]
        self.assertEqual(
            len(device_1.devicecomponent_ids),
            len_devicecomponent_ids + 1,
            msg='\nAdd Componet: '
            + '\n Device: ' + device_1.name
            + '\n len(device_1.user_ids): '
                + str(len(device_1.devicecomponent_ids))
            + '\n len(len_devicecomponent_ids): '
                + str(len_devicecomponent_ids)
        )
        # Remove device component
        len_devicecomponent_ids = len(device_1.devicecomponent_ids)

        device_1.devicecomponent_ids = [
            (self.LIST_REMOVE, self.componets[2].id)]
        self.assertEqual(
            len(device_1.devicecomponent_ids),
            len_devicecomponent_ids - 1,
            msg='\nRemove Componet: '
            + '\n Device: ' + device_1.name
            + '\n len(device_1.user_ids): '
                + str(len(device_1.devicecomponent_ids))
            + '\n len(len_devicecomponent_ids): '
                + str(len_devicecomponent_ids)
        )

        # Check constraints
        # Check Odoo user constraint
        with self.assertRaises(ValidationError):
            device_1.created_by_id = self.test_admin_users[1]

        # Check headquarters constraints
        with self.assertRaises(ValidationError):
            device_1.headquarter_id = self.partner1_addresses[0].id

        # Check device user constraint
        with self.assertRaises(ValidationError):
            device_1.user_ids = [
                (self.LIST_ADD, self.partner1_employees[0].id)]

    def test_create_incidence(self):
        """Incidence model test.
        """
        # Data for checks

        # Optional fields
        observation = 'Unha observación'
        assistance_place = self.incidence_places[0]
        date_end = (datetime.now() + timedelta(days=(10))) \
            .strftime('%Y-%m-%d')

        # Partner0 Devices
        partner0_devices = [
            self.create_device(
                'Usuario0 Equipo1',
                self.test_admin_users[0],
                self.partners[0],
                self.partner0_addresses[0],
            ),
            self.create_device(
                'Usuario0 Equipo2',
                self.test_admin_users[0],
                self.partners[0],
                self.partner0_addresses[1],
            ),
        ]

        # Partner1 Devices
        partner1_devices = [
            self.create_device(
                'Usuario1 Equipo1',
                self.test_admin_users[0],
                self.partners[1],
                self.partner1_addresses[0],
            ),
        ]

        # Incidence 1
        incidence_1 = self.create_incidence(
            self.test_admin_users[0],
            partner0_devices[0].owner_id,
            'Incidencia 1: ' + partner0_devices[0].name,
            'Non se conecta a internet',
        )

        # Check that device is created or not
        assert incidence_1, "Device not created"

        # Optional fields assignment checks
        incidence_1.observation = observation
        self.assertEqual(
            incidence_1.observation,
            observation,
            msg='Add observation'
        )
        incidence_1.assistance_place = assistance_place
        self.assertEqual(
            incidence_1.assistance_place,
            assistance_place,
            msg='Add assistance_place'
        )
        incidence_1.date_end = date_end
        self.assertEqual(
            incidence_1.date_end.strftime('%Y-%m-%d'),
            date_end,
            msg='Add date_end'
        )

        # device_ids assignment checks
        device_ids_list = [
            partner0_devices[1].id
        ]

        # Add device_ids list
        incidence_1.device_ids = [
            (self.LIST_ADD_ALL, 0, device_ids_list)]
        self.assertEqual(
            len(incidence_1.device_ids),
            len(device_ids_list),
            msg='\nAdd Componet: '
            + '\n Incidence: ' + incidence_1.title
            + '\n len(device_1.user_ids): '
                + str(len(incidence_1.device_ids))
            + '\n len(device_ids_list): '
                + str(device_ids_list)
        )
        # Add device to list
        len_device_ids = len(incidence_1.device_ids)

        incidence_1.device_ids = [
            (self.LIST_ADD, partner0_devices[0].id)]
        self.assertEqual(
            len(incidence_1.device_ids),
            len_device_ids + 1,
            msg='\nAdd Componet: '
            + '\n Incidence: ' + incidence_1.title
            + '\n len(device_1.user_ids): '
                + str(len(incidence_1.device_ids))
            + '\n len(len_device_ids): '
                + str(len_device_ids)
        )
        # Remove device from list
        len_device_ids = len(incidence_1.device_ids)

        incidence_1.device_ids = [
            (self.LIST_REMOVE, partner0_devices[1].id)]
        self.assertEqual(
            len(incidence_1.device_ids),
            len_device_ids - 1,
            msg='\nRemove Componet: '
            + '\n Incidence: ' + incidence_1.title
            + '\n len(device_1.user_ids): '
                + str(len(incidence_1.device_ids))
            + '\n len(len_device_ids): '
                + str(len_device_ids)
        )

        # Check constraints
        # Check device_ids constraint
        with self.assertRaises(ValidationError):
            incidence_1.device_ids = [
                (self.LIST_ADD, partner1_devices[0].id)]
        # Check Odoo user constraint
        with self.assertRaises(ValidationError):
            incidence_1.created_by_id = self.test_admin_users[1]

    def create_device(self, name, user, owner, headquarter):
        """Create a device model with the passed data.
        :param name: Device name
        :param user: Odoo user to create device
        :param owner: Device owner
        :param headquarter: Device headquarter
        """
        device = self.Device.sudo(user).create(
            {
                # Required fields
                'created_by_id': user.id,
                'owner_id': owner.id,
                'headquarter_id': headquarter.id,
                'name': name,
                'state': STATE_DEVICE[0][0],
                'date_registration': datetime.now().strftime('%Y-%m-%d'),
            }
        )

        return device

    def create_device_componet(self, product, serial):
        """Create a device component model with the passed data.
        :param product: Product to associate with a device
        :param serial: Serial Number of Product
        """
        componet = self.DeviceComponent.create(
            {
                # Required fields
                'product_id': product.id,
                'date_registration': datetime.now().strftime('%Y-%m-%d'),

                # Optional fields
                'serial': serial,
                'observation': 'Unha observación',
                # 'date_cancellation': '',
            }
        )

        return componet

    def create_incidence(self, user, owner, title, description):
        """Create a device model with the passed data.
        :param user: Odoo user to create device
        :param owner: Device owner
        :param title: Incidence title
        :param description: Incidence description
        """
        incidence = self.Incidence.sudo(user) \
            .create(
                {
                    # Required fields
                    'created_by_id': user.id,
                    'customer_id': owner.id,
                    'title': title,
                    'invoice_id': None,
                    'sale_order_id': None,
                    'failure_description': description,
                    'stage_id': self.incidence_stages[0].id,
                    'date_start': datetime.now().strftime('%Y-%m-%d'),
                }
            )

        return incidence
