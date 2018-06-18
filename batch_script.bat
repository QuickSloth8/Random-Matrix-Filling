for /l %%x in (1, 1, 4) do (
    START CMD /C "python random_matrix_filling.py 10 20 && PAUSE"
)