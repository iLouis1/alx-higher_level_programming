#!/usr/bin/python3
"""Defines unittest for models/rectangle.py."""
import io
import sys
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_instantiation(unittest.TestCase):
    """Unittest, testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        j1 = Rectangle(10, 2)
        j2 = Rectangle(2, 10)
        self.assertEqual(j1.id, j2.id - 1)

    def test_three_args(self):
        j1 = Rectangle(2, 2, 4)
        j2 = Rectangle(4, 4, 2)
        self.assertEqual(j1.id, j2.id - 1)

    def test_four_args(self):
        j1 = Rectangle(1, 2, 3, 4)
        j2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(j1.id, j2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        j = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, j.width)

    def test_width_setter(self):
        j = Rectangle(5, 7, 7, 5, 1)
        j.width = 10
        self.assertEqual(10, j.width)

    def test_height_getter(self):
        j = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, j.height)

    def test_height_setter(self):
        j = Rectangle(5, 7, 7, 5, 1)
        j.height = 10
        self.assertEqual(10, j.height)

    def test_x_getter(self):
        j = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, j.x)

    def test_x_setter(self):
        j = Rectangle(5, 7, 7, 5, 1)
        j.x = 10
        self.assertEqual(10, j.x)

    def test_y_getter(self):
        j = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, j.y)

    def test_y_setter(self):
        j = Rectangle(5, 7, 7, 5, 1)
        j.y = 10
        self.assertEqual(10, j.y)


class TestRectangle_width(unittest.TestCase):
    """Unittests, testing Rectangle width attribute."""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests, testing Rectangle height attribute."""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests, testing Rectangle x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
    """Unittests, testing initialization of Rectangle y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittests, testing Rectangle attribute."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Unittests, testing the area of the Rectangle class."""

    def test_area_small(self):
        j = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, j.area())

    def test_area_large(self):
        j = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, j.area())

    def test_area_changed_attributes(self):
        j = Rectangle(2, 10, 1, 1, 1)
        j.width = 7
        j.height = 14
        self.assertEqual(98, j.area())

    def test_area_one_arg(self):
        j = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            j.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Unittests, testing __str__ and display of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout."""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__ method
    def test_str_method_print_width_height(self):
        j = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(j, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(j.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        j = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(j.id)
        self.assertEqual(correct, j.__str__())

    def test_str_method_width_height_x_y(self):
        j = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(j.id)
        self.assertEqual(correct, str(j))

    def test_str_method_width_height_x_y_id(self):
        j = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(j))

    def test_str_method_changed_attributes(self):
        j = Rectangle(7, 7, 0, 0, [4])
        j.width = 15
        j.height = 1
        j.x = 8
        j.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(j))

    def test_str_method_one_arg(self):
        j = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            j.__str__(1)

    # Test display method
    def test_display_width_height(self):
        j = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(j, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        j = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(j, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        j = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(j, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        j = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(j, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        j = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            j.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests, testing update the Rectangle class."""

    # Test args
    def test_update_args_zero(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(j))

    def test_update_args_one(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(j))

    def test_update_args_two(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(j))

    def test_update_args_three(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(j))

    def test_update_args_four(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(j))

    def test_update_args_five(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(j))

    def test_update_args_more_than_five(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(j))

    def test_update_args_None_id(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(j.id)
        self.assertEqual(correct, str(j))

    def test_update_args_None_id_and_more(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(j.id)
        self.assertEqual(correct, str(j))

    def test_update_args_twice(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(89, 2, 3, 4, 5, 6)
        j.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(j))

    def test_update_args_invalid_width_type(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            j.update(89, "invalid")

    def test_update_args_width_zero(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            j.update(89, 0)

    def test_update_args_width_negative(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            j.update(89, -5)

    def test_update_args_invalid_height_type(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            j.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            j.update(89, 1, 0)

    def test_update_args_height_negative(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            j.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            j.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            j.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            j.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            j.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            j.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            j.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            j.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            j.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            j.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            j.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests, testing update kwargs of the Rectangle class."""

    def test_update_kwargs_one(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(j))

    def test_update_kwargs_two(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(j))

    def test_update_kwargs_three(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(j))

    def test_update_kwargs_four(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(j))

    def test_update_kwargs_five(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(j))

    def test_update_kwargs_None_id(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(j.id)
        self.assertEqual(correct, str(j))

    def test_update_kwargs_None_id_and_more(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(j.id)
        self.assertEqual(correct, str(j))

    def test_update_kwargs_twice(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(id=89, x=1, height=2)
        j.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(j))

    def test_update_kwargs_invalid_width_type(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            j.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            j.update(width=0)

    def test_update_kwargs_width_negative(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            j.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            j.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            j.update(height=0)

    def test_update_kwargs_height_negative(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            j.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            j.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            j.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            j.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        j = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            j.update(y=-5)

    def test_update_args_and_kwargs(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(j))

    def test_update_kwargs_wrong_keys(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(j))

    def test_update_kwargs_some_wrong_keys(self):
        j = Rectangle(10, 10, 10, 10, 10)
        j.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(j))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests, testing to_dictionary of the Rectangle class."""

    def test_to_dictionary_output(self):
        j = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, j.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        j1 = Rectangle(10, 2, 1, 9, 5)
        j2 = Rectangle(5, 9, 1, 2, 10)
        j2.update(**j1.to_dictionary())
        self.assertNotEqual(j1, j2)

    def test_to_dictionary_arg(self):
        j = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            j.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
