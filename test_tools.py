#def add(a, b):
#    return a + b

#def test_add():
#    assert add(2,3) == 5

#def test_add_negtives():
#    assert add(-1, -1) == -2

#def test_add_zero():
#    assert add(0, 5) == 5 

from run_checks import check_tool

def test_tool_exists():
    assert check_tool("git") == True  # test a tool you know is installed

def test_tool_missing():
    assert check_tool("ttu") == False  # test a fake tool that doesn't exist
