from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from app import MENU_PROMPT


class AppTest(TestCase):

    def test_input(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)


    def test_menu_calls_print_blog(self):
        with patch('app.print_blogs') as mocked_menu:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_menu.assert_called()


    def test_print_blogs(self):

        blog = Blog('Test', 'Test Author')
        app.blogs = {'test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))
