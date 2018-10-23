from api.request import Request
import unittest


class ValidationTest(unittest.TestCase):
    def test_get_field_rules(self):
        string_rules = 'required|min:10|max:20'
        rules = Request.get_field_rules(string_rules)
        self.assertEqual(['required', 'min:10', 'max:20'], rules)

    def test_get_request_rules(self):
        data = {"username": "joma", "password": "1234"}
        request_schema = {'username': 'required|min:10|max:20',
                          'password': 'required|min:10|max:20'}
        request = Request(data, request_schema)
        all_rules = request.get_request_rules()
        self.assertEqual({'password': ['required', 'min:10', 'max:20'],
                          'username': ['required', 'min:10', 'max:20']},
                         all_rules)

    def test_get_value(self):
        data = {"username": "joma", "password": "1234"}
        request_schema = {'username': 'required|min:10|max:20',
                          'password': 'required|min:10|max:20'}
        request = Request(data, request_schema)
        self.assertTrue(request.get_value("username"))
        self.assertFalse(request.get_value("name"))
        self.assertEqual("joma", request.get_value("username"))

    def test_validate_field(self):
        data = {"username": "", "password": "1234"}
        request_schema = {'username': 'required|min:10|max:20',
                          'password': 'required|min:10|max:20',
                          }
        request = Request(data, request_schema)
        field_rules = ['required', 'min:10', 'max:20']
        field = "username"
        errors = request.validate_field(field, field_rules)
        self.assertEqual(['username is required'], errors)

    def test_validate_request(self):
        data = {"username": "", "password": "1234"}
        request_schema = {'username': 'required|min:10|max:20',
                          'password': 'required|min:10|max:20',
                          'name': 'required|min:10|max:20',
                          }
        request = Request(data, request_schema)
        self.assertTrue(request.validate())
        self.assertEqual({'errors': {'username': ['username is required'],
                                     'name': ['name is required']}},
                         request.validate())

    def test_valid_request(self):
        data = {"username": "joma", "password": "1234","name":"joma simeon"}
        request_schema = {'username': 'required|min:10|max:20',
                          'password': 'required|min:10|max:20',
                          'name': 'required|min:10|max:20',
                          }
        request = Request(data, request_schema)
        self.assertEqual(None,request.validate())
