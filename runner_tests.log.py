WARNING:root:Неверный тип данных для объекта Runner
Traceback (most recent call last):
  File "C:\Users\adeli\PycharmProjects\module_13_1\tests_12_4.py", line 19, in test_run
    begun = Runner(31331)
            ^^^^^^^^^^^^^
  File "C:\Users\adeli\PycharmProjects\module_13_1\rt_with_exceptions.py", line 6, in __init__
    raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
TypeError: Имя может быть только строкой, передано int
WARNING:root:Неверная скорость для Runner
Traceback (most recent call last):
  File "C:\Users\adeli\PycharmProjects\module_13_1\tests_12_4.py", line 9, in test_walk
    peshehod = Runner('Пешеход', -3)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\adeli\PycharmProjects\module_13_1\rt_with_exceptions.py", line 11, in __init__
    raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
ValueError: Скорость не может быть отрицательной, сейчас -3