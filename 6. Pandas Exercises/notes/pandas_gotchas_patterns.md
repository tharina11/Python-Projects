# Pandas Gotchas & Patterns (Interview + Project Reference)

> **Purpose**: Collect pandas patterns and common mistakes to refer in
future coding projects.

---

## 1. Dates & Time Series
```python
price['date'] = pd.to_datetime(price['date'])
```

**Why it matters**  
Without this, Pandas treats dates as strings (`object`). Time-based operations break.

**🧠 Mental rule** 
> If time matters → convert to datetime immediately

---

## 2. Resample and transform
```python
price['monthly_avg'] = price.resample('M')['close'].mean()
```

- `resample()` returns one row per period (month-end)
- Assignment aligns by index → only month-end matches

```python
price['monthly_avg'] = (
    price['close']
    .resample('M')
    .transform('mean')
)
```

**🧠 Mental rule**  
> Use `transform()` when you want group values repeated per row
> `agg()` reduces rows, `transform()` preserves rows

---

## 3. Filtering & Assignment

### Chained indexing
```python
df['trend'][df['close'] > 100] = 'up'
```

**Why bad**  
- Ambiguous
- Can fail silently
- Triggers `SettingWithCopyWarning`

** Correct pattern**  
```python
df.loc[df['close'] > 100, 'trend'] = 'up'
```

**🧠 Mental rule**  
> Use `.loc` for every conditional assignment

---

## 4. `.loc` vs `.iloc`

| Method | Uses | Example |
|-----|-----|-----|
| `.loc` | Labels | `df.loc['2024-01-01', 'close']` |
| `.iloc` | Positions | `df.iloc[0, 2]` |

**🧠 Mental rule**  
> `.loc` = names, `.iloc` = numbers

## 5. Pandas thinking pattern


Most confusion happens because:

- People focus on what they want to change

- Pandas requires you to state where first

### Example
```python
df.loc[df['Close'] > df['Open'], 'Gain'] = True

```

**How to read**  
- In df, at rows where Close > Open, in column Gain, assign True

** Correct pattern**  
```python
df.loc[df['close'] > 100, 'trend'] = 'up'
```

**🧠 Mental rule**  
> .loc is declarative, not procedural. 
- You don’t “step through”

- You describe a state


