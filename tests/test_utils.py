import os
import unittest
from unittest.mock import mock_open, patch

from src.utils import fin_transaction


class TestFinTransaction(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
    def test_fin_transaction_success(self, mock_file):
        result = fin_transaction('test.json')
        self.assertEqual(result, [{"id": 1, "amount": 100}])
        mock_file.assert_called_once_with(os.path.join('..', 'data', 'test.json'), 'r', encoding='utf-8')

    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_fin_transaction_empty_file(self, mock_file):
        result = fin_transaction('empty.json')
        self.assertEqual(result, [])

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_fin_transaction_file_not_found(self, mock_file):
        result = fin_transaction('non_existent.json')
        self.assertEqual(result, [])
