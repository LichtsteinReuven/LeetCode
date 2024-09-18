/*
    Table: Products
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | product_id  | int     |
    | low_fats    | enum    |
    | recyclable  | enum    |
    +-------------+---------+
    product_id is the primary key (column with unique values) for this table.
    low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
    recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

    Write a solution to find the ids of products that are both low fat and recyclable.

    Return the result table in any order.

    The result format is in the following example.

    Example 1:
    Input:
    Products table:
    +-------------+-----------+-------------+
    | product_id  | low_fats  | recyclable  |
    +-------------+-----------+-------------+
    | 1           | Y         | N           |
    | 2           | N         | Y           |
    | 3           | Y         | Y           |
    | 4           | N         | Y           |
    | 5           | Y         | N           |
    +-------------+-----------+-------------+
    Output:
    +-------------+
    | product_id  |
    +-------------+
    | 3           |
    +-------------+

    Explanation:
    Product 1 is low fat but not recyclable.
    Product 2 is recyclable but not low fat.
    Product 3 is low fat and recyclable.
    Product 4 is recyclable but not low fat.
    Product 5 is low fat but not recyclable.
 */

SELECT product_id
FROM Products
WHERE low_fats = 'Y'
AND recyclable = 'Y';