import sys
import os
import unittest
import json
from unittest.mock import patch
sys.path.append(os.path.abspath('..'))
from app import app, Translator, subjects

class TestTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = Translator()

    def test_get_random_subject_valid_subject(self):
        subject = "colors"
        answer_translation, question_translation, options = self.translator.get_random_subject(subject)

        # Check if the returned values are as expected
        self.assertIn(answer_translation, subjects[subject].keys())
        self.assertIn(question_translation, subjects[subject].values())
        self.assertEqual(len(options), 4)  # 1 correct answer + 3 distractors
        self.assertIn(answer_translation, options)

    def test_get_random_subject_invalid_subject(self):
        subject = "shapes"  # Invalid subject
        result = self.translator.get_random_subject(subject)
        self.assertIsNone(result)

    def test_api_get_question_valid_parameters(self):
        with app.test_client() as client:
            response = client.get('/api/get_question?subject=colors&answer_lang=en&question_lang=mi')
            data = json.loads(response.data.decode('utf-8'))

            self.assertEqual(response.status_code, 200)
            self.assertIn('question', data)
            self.assertIn('options', data)
            self.assertIn('answer', data)

    def test_api_get_question_invalid_subject(self):
        with app.test_client() as client:
            response = client.get('/api/get_question?subject=shapes&answer_lang=en&question_lang=mi')
            data = json.loads(response.data.decode('utf-8'))

            self.assertEqual(response.status_code, 400)
            self.assertIn('error', data)
            self.assertEqual(data['error'], 'Invalid parameters')

    def test_api_get_question_invalid_parameters(self):
        with app.test_client() as client:
            # Missing subject parameter
            response = client.get('/api/get_question?answer_lang=en&question_lang=mi')
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', data)
            self.assertEqual(data['error'], 'Invalid parameters')

            # Invalid answer_lang parameter
            response = client.get('/api/get_question?subject=colors&answer_lang=fr&question_lang=mi')
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', data)
            self.assertEqual(data['error'], 'Invalid parameters')

            # Invalid question_lang parameter
            response = client.get('/api/get_question?subject=colors&answer_lang=en&question_lang=es')
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', data)
            self.assertEqual(data['error'], 'Invalid parameters')


if __name__ == '__main__':
    unittest.main()
