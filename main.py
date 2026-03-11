import numpy as np
import logging

#настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)
matrix = np.array([
    [6, 12, 20, 24],
    [9, 7, 9, 28],
    [23, 18, 15, 19],
    [27, 24, 21, 15]
])
logger.info("введение матрицы")

#Критерий Вальда
max_in_line = np.max(matrix, axis=1)
min_index = np.argmin(max_in_line)
logger.info(f"Вальд")

#Критерий Сэвинжа
min_in_columns = np.min(matrix, axis=0)
result = matrix - min_in_columns
max_in_lineR = np.max(result, axis=1)
max_indexR = np.argmin(max_in_lineR)
logger.info(f"Сэвидж")

#Критерий Гурвица исходная матрица
p = 0.5
row_minA = np.min(matrix, axis=1)
row_maxA = np.max(matrix, axis=1)
HA = p * row_minA + (1 - p) * row_maxA
indexA = np.argmin(HA)
logger.info(f"Гурвиц (Исходная)")

#Критерий Гурвица матрицы риска
row_minR = np.min(result, axis=1)
row_maxR = np.max(result, axis=1)
HR = p * row_minR + (1 - p) * row_maxR
indexR = np.argmin(HR)
logger.info(f"Гурвиц (Риска)")

print("\nОтсчет")
print(f"Вальд: Стратегия {min_index+1}")
print(f"Сэвидж: Стратегия {max_indexR+1}")
print(f"Гурвиц (Исходная): Стратегия {indexA+1}")
print(f"Гурвиц (Риска): Стратегия {indexR+1}")
