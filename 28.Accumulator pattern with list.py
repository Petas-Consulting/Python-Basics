nums = [3, 5, 8]
accum = []
for w in nums:
    x = w**2
    accum.append(x)
print(accum)
'''
Here, we initialize the accumulator variable to be an empty list, on line 2.

We iterate through the sequence (line 3). On each iteration we transform the item by squaring it (line 4).

The update step appends the new item to the list which is stored in the accumulator variable (line 5). 
The update happens using the .append(), which mutates the list rather than using a reassignment. 
Instead, we could have written accum = accum + [x], or accum += [x]. In either case, we’d need to concatenate a list containing x, not just x itself.

At the end, we have accumulated a new list of the same length as the original, but with each item transformed into a new item. This is called a mapping operation, and we will revisit it in a later chapter.

Note how this differs from mutating the original list, as you saw in a previous section.'''
