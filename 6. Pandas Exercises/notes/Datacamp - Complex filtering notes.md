## **Pandas most common patterns - Complex Filtering**

Design questions (think through before you code) - What are the input columns? -> Which formula we need to apply?


### 1. Selecting top N

Both nlargest() and nsmallest() functions can be applied. (Operation order: 1. Sort, 2. Slice)

```python
top_n_df = df.nlargest(n, 'column_name')
bottom_n_df = df.nsmallest(n, 'column_name')
```


### 2. Direct calculations in filtering

Use expressions directly in filtering in simple cases.

```python
filtered_df = df.loc[
    (df['col_1'] <= 10) |
    (df['col_2'] / df['col_3'] > 0.25)]
```


### 3. Intermediate Columns

1. Break the calculation into multiple steps.

2. Create boolean intermediate columns with descriptive names. Use them to filter. 

3. Drop the intermediate columns after the calculation.

```python
df['condition1'] = (df['col_1'] <= 10)
df['condition2'] = (df['col_2'] > 0)
df['condition3'] = (df['col_1'] < df['col_3'])

filtered_df = df.loc[df['condition1'] &
                     (df['condition2'] |
                      df['condition3'])]
```

### 4. Condition inversion - Complement

Use NOT operation (~) to negate a condition. Always enclose the compound operation in parentheses when using ~.

```python
df_complement = df.loc[
    ~((df['col_1'] <= 10) |
      (df['col_2'] / df['col_3'] > 0.25))]
```

### 5. Result Verification

Complex filtering is prone to errors. Always verify results during calculation and after calculation.

1. While building — Verify each intermediate column works correctly on its own

2. After building — Verify the final filtered result includes the right rows and excludes the right rows

Pick a few rows and check them by hand