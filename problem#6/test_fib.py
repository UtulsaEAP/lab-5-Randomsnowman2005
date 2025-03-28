from fib import fibonacci

def test_passed():
    # Test case 1
    result = fibonacci(7)
    assert result == 13


# Test case 2
def test_passed_2():
    result = fibonacci(0)
    assert result == 0

# Test case 3
def test_passed_3():
    result = fibonacci(2)
    assert result == 1
      

# Test case 4
def test_passed_4():
    result = fibonacci(2)
    assert result == 1

# Example usage
# result_1 = test_passed()
# print(result_1)

# result_2 = test_passed_2()
# print(result_2)

# result_3 = test_passed_3()
# print(result_3)

# result_4 = test_passed_4()
# print(result_4)
