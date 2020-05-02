from .test_common import TestCommonData


class XestionsatTestDevice(TestCommonData):
    '''Test.
    '''

    def setUp(self):
        super(XestionsatTestDevice, self).setUp()
        self.Device = self.env['xestionsat.device']

    def test_create_device(self):
        '''Test.
        '''

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
                # 'user_ids': self.partner_1_employee_1,
                # 'devicecomponents_ids': 'xestionsat.device.component',
                # 'internal_id': '',
                # 'location': '',
                # 'description': '',
                # 'observation': '',
                # 'date_registration': '',
                # 'date_cancellation': '',
            }
        )

        # Check that device is created or not
        assert self.device_1, "Device not created"
