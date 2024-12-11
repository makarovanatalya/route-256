###Conditions

There are n boxes of apples (an even number) in a warehouse.
The storekeeper wants to form n/2 pallets. Each pallet must consist of exactly two boxes. Two boxes can lie stably on a pallet only if their weight is the same.
The boxes can be filled with apples, each of which increases the weight of the box by one.
The storekeeper wants to know what is the minimum number of apples that must be added to the boxes to form exactly n/2 pallets (that is, each pair of boxes must lie on the pallet). Your task is to find this number.

###Input data format

The first line of the input data contains one integer n (2 ≤ n ≤ 100) — the number of boxes. It is guaranteed that n is always an even number.
The second line of input contains n integers a1, a2, …, an (1 ≤ a[i] ≤ 100), where a[i] is equal to the weight of the i-th box.

###Output format

Print one integer — the minimum number of apples that must be put into the boxes to form exactly n/2 pallets.