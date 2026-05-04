## **Pandas most common patterns**

Design questions (think through before you code) - By which column do we aggregate? -> Which column to summarize? -> Which operation to apply?

## Filtering


### 1. .loc[]

There are 3 ways you can use loc[].

1. Select columns only:

```python
df.loc[:, ['col1', 'col2']]
```

2. Select rows only:

```python
df.loc[condition]
```

3. Select both rows and column at once:

```python
df.loc[condition, ['col1', 'col2']]
```

Selecting a single column using the column name returns a Pandas Series and is suitable for applying methods to a single column.


### 2. Partial String matching

Three patterns used:

```python
df.loc[df['col_1'].str.contains('value')]
df.loc[df['col_1'].str.startswith('value')]
df.loc[df['col_1'].str.endswith('value')]
```


### 3. Missing values

In pandas missing numerical values are shown as *NaN* and missing strings are shown as *none*. Both represent missing or non-existent data. *isna()* is used to identify missing data. *notna()* is the opposite of *isna()*.

1. Find rows with missing values
```python
df.loc[df['col_1'].isna()]
```

2. Find rows with values
```python
df.loc[df['col_1'].notna()]
```
