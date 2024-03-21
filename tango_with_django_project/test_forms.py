from django.test import TestCase
from tenrr.forms import PostForm

class PostFormTest(TestCase):
    def test_post_form_valid_data(self):
        form = PostForm(data={
            'title': 'Test Post',
            'content': 'Test Content',
            'price': 10.00
        })
        self.assertTrue(form.is_valid())

    def test_post_form_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3) 

    def test_post_form_invalid_price(self):
        form = PostForm(data={
            'title': 'Test Post',
            'content': 'Test Content',
            'price': 'invalid'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertEqual(form.errors['price'][0], 'Enter a valid number.')

    def test_post_form_negative_price(self):
        form = PostForm(data={
            'title': 'Test Post',
            'content': 'Test Content',
            'price': -10.00
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertEqual(form.errors['price'][0], 'Ensure this value is greater than or equal to 0.')

    def test_post_form_missing_title(self):
        form = PostForm(data={
            'content': 'Test Content',
            'price': 10.00
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_form_missing_content(self):
        form = PostForm(data={
            'title': 'Test Post',
            'price': 10.00
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_post_form_missing_price(self):
        form = PostForm(data={
            'title': 'Test Post',
            'content': 'Test Content',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertEqual(form.errors['price'][0], 'This field is required.')
