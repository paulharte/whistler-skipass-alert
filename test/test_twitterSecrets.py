from unittest import TestCase

from whistler.tweeter.secrets import TwitterSecrets, TwitterSecretException


class TestTwitterSecrets(TestCase):
    def test_secrets(self):
        test_key = "thisisakey"
        secrets = TwitterSecrets({"consumer": {"key": test_key}})

        self.assertEqual(test_key, secrets.get_consumer_key())

    def test_exception(self):
        ex = TwitterSecretException("message")
        self.assertIn("Example", str(ex.args))
