import torch
import adder
import pathlib

def test_add():
    assert adder.add(2,3) == 5

def test_add2():
    assert adder.add(3, -3) == 0

def test_add3():
    assert adder.add3(1, 2, 3) == 6

def test_gpu():
    #assert torch.cuda.is_available()
    pass

def test_artifact():
    pathlib.Path('logs').mkdir(parents=True, exist_ok=True)
    with open('logs/test_output.log', 'w') as fout:
        print('Test output', file=fout)
