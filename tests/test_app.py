import unittest
import json
from app import app, MANGO_IMPORT_CONDITIONS

class MangoImportTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        """Test the home page route"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Australian Mango Import Conditions', response.data)

    def test_get_countries(self):
        """Test the countries API endpoint"""
        response = self.app.get('/api/countries')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        # Check if all countries are present
        expected_countries = ["Thailand", "India", "Pakistan", "Philippines", 
                            "Vietnam", "Taiwan", "Mexico", "Fiji", "Haiti"]
        self.assertEqual(sorted(data), sorted(expected_countries))

    def test_get_conditions_valid_country(self):
        """Test getting conditions for a valid country"""
        response = self.app.get('/api/conditions/Thailand')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        # Check structure and content
        self.assertIn('permits_required', data)
        self.assertIn('treatments', data)
        self.assertIn('documentation', data)
        self.assertIn('additional_requirements', data)
        self.assertIn('bicon_link', data)

        # Verify specific data for Thailand
        self.assertIn('Vapor Heat Treatment (VHT)', data['treatments'])
        self.assertIn('Import Permit', data['permits_required'])

    def test_get_conditions_invalid_country(self):
        """Test getting conditions for an invalid country"""
        response = self.app.get('/api/conditions/InvalidCountry')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, {})

    def test_data_consistency(self):
        """Test consistency of data structure across all countries"""
        required_keys = ['permits_required', 'treatments', 'documentation', 
                        'additional_requirements', 'bicon_link']
        
        for country in MANGO_IMPORT_CONDITIONS:
            conditions = MANGO_IMPORT_CONDITIONS[country]
            for key in required_keys:
                self.assertIn(key, conditions)
                self.assertIsInstance(conditions[key], list)

    def test_bicon_links(self):
        """Test that all BICON links are valid format"""
        for country in MANGO_IMPORT_CONDITIONS:
            conditions = MANGO_IMPORT_CONDITIONS[country]
            self.assertTrue(conditions['bicon_link'].startswith('https://'))
            self.assertIn('bicon.agriculture.gov.au', conditions['bicon_link'])

if __name__ == '__main__':
    unittest.main()
