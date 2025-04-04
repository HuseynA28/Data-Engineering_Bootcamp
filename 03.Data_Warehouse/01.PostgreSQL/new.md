# SQL Query Guide

Welcome to the **SQL Query Guide**! This comprehensive guide will help you understand and construct SQL queries to interact with your `classicmodels` database effectively. Whether you're retrieving data, filtering results, or performing aggregations, this guide covers essential SQL concepts with clear examples.

---

## Table of Contents

1. [Selecting Data](#selecting-data)
   - [Select All Data](#select-all-data)
   - [Select Specific Columns](#select-specific-columns)
   - [Select Unique Rows](#select-unique-rows)
2. [Aggregation Functions](#aggregation-functions)
   - [COUNT Function](#count-function)
   - [Count Unique Values](#count-unique-values)
3. [Filtering Data](#filtering-data)
   - [WHERE Clause](#where-clause)
   - [Combining Conditions](#combining-conditions)
4. [Sorting and Limiting Results](#sorting-and-limiting-results)
   - [ORDER BY Clause](#order-by-clause)
   - [LIMIT Clause](#limit-clause)
5. [Advanced Filtering](#advanced-filtering)
   - [BETWEEN and IN Operators](#between-and-in-operators)
   - [Pattern Matching with LIKE](#pattern-matching-with-like)
   - [NOT LIKE Operator](#not-like-operator)
6. [Common Pitfalls & Fixes](#common-pitfalls--fixes)

---

## Selecting Data

### Select All Data
Retrieve all rows and columns from the `customers` table.

```sql
SELECT * FROM classicmodels.customers;
```

- `*`: Fetches all columns.
- `classicmodels.customers`: Specifies the database (`classicmodels`) and table (`customers`).

### Select Specific Columns
Retrieve only specific columns, such as `customerName` and `addressLine1`.

```sql
SELECT customerName, addressLine1
FROM classicmodels.customers;
```

- List the desired columns separated by commas.
- Always specify the table after `FROM`.

### Select Unique Rows
Remove duplicate values from a column to get unique entries, such as unique `country` values.

```sql
SELECT DISTINCT country
FROM classicmodels.customers;
```

- `DISTINCT`: Returns only unique values from the specified column.

---

## Aggregation Functions

### COUNT Function
Counts the number of rows or non-null values in a column.

#### Basic Syntax

```sql
-- Count all rows in the table
SELECT COUNT(*) FROM classicmodels.customers;

-- Count non-null values in a specific column
SELECT COUNT(customerName) FROM classicmodels.customers;
```

- `COUNT(*)`: Counts all rows, including those with `NULL` values.
- `COUNT(columnName)`: Counts non-null values in the specified column.

### Count Unique Values
Count distinct values in a column, such as the number of unique `city` values.

```sql
SELECT COUNT(DISTINCT city) FROM classicmodels.customers;
```

---

## Filtering Data

### WHERE Clause
Filters rows based on specified conditions.

#### Basic Syntax

```sql
SELECT column1, column2
FROM table
WHERE condition;
```

#### Example
Get customers from `France` or the `USA`.

```sql
SELECT customerName
FROM classicmodels.customers
WHERE country = 'France' OR country = 'USA';
```

### Combining Conditions
Use logical operators (`AND`, `OR`, `NOT`) to combine multiple conditions.

#### Example
Retrieve customers from `France` with a credit limit over `$50,000`.

```sql
SELECT customerName, creditLimit
FROM classicmodels.customers
WHERE country = 'France' AND creditLimit > 50000;
```

---

## Sorting and Limiting Results

### ORDER BY Clause
Sorts results by specified column(s) in ascending (`ASC`) or descending (`DESC`) order.

#### Basic Syntax

```sql
SELECT column1, column2
FROM table
ORDER BY column [ASC|DESC];
```

#### Example
Sort customers by credit limit (highest to lowest):

```sql
SELECT customerName, creditLimit
FROM classicmodels.customers
ORDER BY creditLimit DESC;
```

### LIMIT Clause
Restricts the number of rows returned. Often paired with `ORDER BY` for "top N" queries.

#### Example
Get the top 3 customers by credit limit:

```sql
SELECT customerName, creditLimit
FROM classicmodels.customers
ORDER BY creditLimit DESC
LIMIT 3;
```

---

## Advanced Filtering

### BETWEEN and IN Operators

#### BETWEEN Operator
Filters values within a specified range (inclusive of endpoints).

```sql
SELECT COUNT(*)
FROM classicmodels.orders
WHERE orderDate BETWEEN '2003-01-16' AND '2003-04-16';
```

#### IN Operator
Checks if a value matches any value in a list.

```sql
SELECT customerName, country
FROM classicmodels.customers
WHERE country IN ('Azerbaijan', 'France', 'USA');
```

---

## Pattern Matching with LIKE

### LIKE Operator Basics
Matches string patterns using wildcards:

| Wildcard | Description | Example |
|----------|------------|---------|
| `%`      | Matches any sequence of characters | `'A%'` → "Apple", "Antelope" |
| `_`      | Matches exactly one character | `'_at'` → "Cat", "Bat" |

#### Example
Find employees with first names starting with "A":

```sql
SELECT *
FROM classicmodels.employees
WHERE firstName LIKE 'A%';
```

---

## NOT LIKE Operator
Exclude rows matching a pattern.

```sql
SELECT *
FROM classicmodels.customers
WHERE customerName NOT LIKE '%nal%';
```

---

## Common Pitfalls & Fixes

### Problem: Missing Single-Digit Dates
Incorrect approach:

```sql
SELECT COUNT(*)
FROM classicmodels.payments
WHERE paymentDate LIKE '2004-05-__';
```

Correct approach:

```sql
SELECT COUNT(*)
FROM classicmodels.payments
WHERE paymentDate LIKE '2004-05-%';
```

Ensure that your date patterns account for all possible formats and values.
