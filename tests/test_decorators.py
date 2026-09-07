import os

import pytest

from src.decorators import log


def test_log_success(capsys):
    @log(filename=None)
    def add_func(a, b):
        return a + b

    result = add_func(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    assert "add_func: ok" in captured.out


def test_log_error(capsys):
    @log(filename=None)
    def my_func(x: int, y: int) -> int:
        return x ** y

    with pytest.raises(TypeError):
        my_func("1", 2)

    captured = capsys.readouterr()

    assert "unsupported operand type" in captured.out
    assert "Inputs: ('1', 2), {}" in captured.out


def test_log_capsys(capsys):
    @log(filename=None)
    def hello_world():
        return "Hello, world!"

    hello_world()

    captured = capsys.readouterr()
    assert "hello_world: ok" in captured.out
    assert "Time work:" in captured.out


def test_log_writes_to_file(tmp_path):
    log_file = tmp_path / "my_log.txt"

    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    result = my_function(10, 20)

    assert result == 30  # Функция возвращает сумму, а не строку!
    assert log_file.exists()

    content = log_file.read_text(encoding="utf-8")
    assert "my_function: ok" in content
    assert "Time work:" in content


def test_log_kwargs(capsys):
    @log(filename=None)
    def greeting(name, greeting='Hello'):
        return f'{greeting}, {name}!'

    result = greeting('Alice')
    assert result == 'Hello, Alice!'
    captured = capsys.readouterr()
    assert "greeting: ok" in captured.out


def test_log_preserves_function_name():
    @log(filename=None)
    def secret_operation():
        pass

    assert secret_operation.__name__ == "secret_operation"
