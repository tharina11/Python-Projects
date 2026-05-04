## Pandas most common patterns

Design questions (think through before you code) - By which column do we aggregate? -> Which column to summarize? -> Which operation to apply?

### 1. Aggregation

```python
grouped_df = df.groupby('grouping_column')

summary_df = grouped_df.agg(
    total_count=('column_1', 'count'),
    total_amount=('column_2', 'sum')
)

summary_df = summary_df.reset_index()
summary_df = summary_df.sort_values(by = 'total_amount', ascending = False)
```
Single chained operation

```python
summary_df = df.groupby('grouping_column').agg(
    total_count=('column_1', 'count'),
    total_amount=('column_2', 'sum')
).reset_index()
```
Group aggregations work through three steps. 

- 1. Split : Divide data into groups

- 2. Apply : Apply summary operation in each group

- 3. Combine : Results in each group are combined

### 2. Uniqueness

```python
df['column_name'].unique()
```

Explore unique values before you aggregate to find unexpected scenarios.

### 3. Frequency

Use codes below to get counts and proportions in frequency analysis.

```python
df['column_name'].value_counts()
df['column_name'].value_counts(normalize=True)
```

### 4. Sorting

```python
summary_df = summary_df.sort_values(by='total_amount', ascending=False)
```






