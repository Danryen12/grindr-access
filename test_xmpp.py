import unittest
from unittest.mock import patch
from xmpp import connect

class TestConnect(unittest.TestCase):
    @patch('socket.create_connection')
    @patch('ssl.create_default_context')
    def test_connect_success(self, mock_create_default_context, mock_create_connection):
        # Mock the return values and behavior of the socket and ssl modules
        mock_context = mock_create_default_context.return_value
        mock_sock = mock_create_connection.return_value.__enter__.return_value
        mock_secure_sock = mock_context.wrap_socket.return_value.__enter__.return_value

        # Set up the expected values
        expected_hostname = "chat.grindr.com"
        expected_plain_token = "your_plain_token"
        expected_encoded_message = "<session to='chat.grindr.com' auth_data='your_plain_token' resource='3e6f228230b9c7b3' stream_management='true' carbons='true' compress='false'>".encode()
        expected_response = b"Response from server"

        # Call the function under test
        with patch('builtins.print') as mock_print:
            mock_secure_sock.recv.return_value = expected_response
            connect(expected_plain_token)

        # Assert that the socket and ssl functions were called with the expected arguments
        mock_create_connection.assert_called_once_with((expected_hostname, 453))
        mock_create_default_context.assert_called_once_with()
        mock_context.wrap_socket.assert_called_once_with(mock_sock, server_hostname=expected_hostname)

        # Assert that the message was sent and received correctly
        mock_secure_sock.send.assert_called_once_with(expected_encoded_message)
        mock_secure_sock.recv.assert_called_once_with(2048)

        # Assert that the received message was printed
        mock_print.assert_called_once_with(expected_response.decode())

if __name__ == '__main__':
    unittest.main()