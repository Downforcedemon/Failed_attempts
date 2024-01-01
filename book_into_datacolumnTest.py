from  unittest.mock import patch,MagicMock
import unittest
import os
import psycopg2
import book_into_dataColumn

# Assuming your original code is in a file named 'book_into_dataColumn.py'

import sys
sys.path.append('/home/kali/Downloads/PythonScripts')  # Add the directory containing the missing module
from book_into_dataColumn import read_file_as_binary

class TestBookIntoDataColumn(unittest.TestCase):
    def setUp(self):
        self.test_file_path = '/home/kali/Downloads/Culture_Series/ConsiderPhlebas.epub'

    def test_read_file_as_binary(self):
        expected_content = b'This is some test content'
        with open(self.test_file_path, 'wb') as test_file:
            test_file.write(expected_content)

        actual_content = read_file_as_binary(self.test_file_path)
        self.assertEqual(actual_content, expected_content)

    @patch('psycopg2.connect')
    def test_insert_into_database(self, mock_connect):
        mock_conn = MagicMock()
        mock_cur = MagicMock()

        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur

        binary_content = read_file_as_binary(self.test_file_path)

        query = """                      
        UPDATE Books
        SET bookcontent = %s              
        WHERE bookid = 11 and title = 'Consider Phlebas: A Culture Novel';
        """

        mock_cur.execute(query, (psycopg2.Binary(binary_content),))

        mock_connect.assert_called_once_with("dbname=Sci-fi user=postgres host=192.168.0.48 password = password")
        mock_conn.cursor.assert_called_once()
        mock_cur.execute.assert_called_once_with(query, (psycopg2.Binary(binary_content),))
        mock_conn.commit.assert_called_once()
        mock_cur.close.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()