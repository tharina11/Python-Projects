## **Pandas Transformations**

Design questions (think through before you code) - What are the input columns? -> Which formula we need to apply?


### 1. Calculating percent of totals

```python
df["col_a_pot"] = (100 * df["col_a"] /
                   df["col_a"].sum())

df["col_a_pot"] = round(df["col_a_pot"], 2)


```
Be aware of the negative values in the column, which could drive the percentage values up.

### 2. Multi-Step Transformations

1. Break the calculation into multiple steps.

2. Name intermediate columns descriptively.

3. Drop the intermediate columns after the calculation.