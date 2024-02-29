class Stack:
    def __init__(self):
        self.data = []

    def push(self, el):
        self.data.append(el)

    def pop(self):
        return self.data.pop()

    def top(self):
        topmost_element = self.data[-1]
        return topmost_element

    def is_empty(self):
        if not self.data:
            result = True
        else:
            result = False
        return result

    def __str__(self):
        reversed_data = reversed(self.data)
        result = ", ".join(f"{el}" for el in reversed_data)
        return f"[{result}]"


# test zero
import unittest


class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push("apple")
        stack.push("carrot")
        self.assertEqual(str(stack), '[carrot, apple]')
        self.assertEqual(stack.pop(), 'carrot')
        self.assertEqual(stack.top(), 'apple')
        stack.push("cucumber")
        self.assertEqual(str(stack), '[cucumber, apple]')
        self.assertEqual(stack.is_empty(), False)


if __name__ == '__main__':
    unittest.main()
