#!/usr/bin/python3
"""
This module defines a VerboseList class.
"""


class VerboseList(list):
    """
    A list subclass that prints a message whenever it is modified.
    """

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend the list and print a notification."""
        initial_len = len(self)
        super().extend(iterable)
        added_count = len(self) - initial_len
        print(f"Extended the list with {added_count} items.")

    def remove(self, item):
        """Remove an item and print a notification."""
        if item in self:
            print(f"Removed {item} from the list.")
            super().remove(item)
        else:
            # Replicating original ValueError behavior for non-existent items
            super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a notification."""
        # Need to fetch the item to print it before removal
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)


# Testing the class
if __name__ == "__main__":
    v_list = VerboseList()

    v_list.append(10)
    v_list.extend([20, 30, 40])
    v_list.remove(20)
    v_list.pop()
    v_list.pop(0)
