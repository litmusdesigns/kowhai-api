import unittest
from app import Translator, subjects

class TestTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = Translator()

    def test_get_random_subject_valid_subject(self):
        a_lang = 'en'
        q_lang = 'mi'
        subject = 'colors'

        result = self.translator.get_random_subject(subject, a_lang, q_lang)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)

        answer_translation, question_translation, options = result
        self.assertIsNotNone(answer_translation)
        self.assertIsNotNone(question_translation)
        self.assertIn(answer_translation, subjects[subject][a_lang].values())
        self.assertIn(question_translation, subjects[subject][q_lang].values())
        self.assertEqual(len(options), 4)
        self.assertIn(answer_translation, options)
        self.assertEqual(len(set(options)), len(options))

    def test_get_random_subject_invalid_inputs(self):
        invalid_cases = [
            ('invalid_subject', 'en', 'mi'),
            ('numbers', 'en', 'fr'),
            ('invalid_subject', 'de', 'fr')
        ]

        for subject, a_lang, q_lang in invalid_cases:
            with self.subTest(subject=subject, a_lang=a_lang, q_lang=q_lang):
                result = self.translator.get_random_subject(subject, a_lang, q_lang)
                self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
