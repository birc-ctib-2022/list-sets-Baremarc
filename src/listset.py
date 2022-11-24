"""List implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar
)

T = TypeVar('T')


class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]

    def __init__(self, init: Iterable[T]) -> None:
        """Initialise set with init."""
        self.data=list[init]
        ...  # FIXME

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        ...  # FIXME
        for x in self.data:
            print('We fount it')

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        ... 
        if self.data==[]:
            return True 
        # FIXME

    def add(self, x: T) -> None:
        """Add x to the set."""
        ...  # FIXME
        return self.data.append(x)

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        ...  # FIXME
        return self.data.remove(x)
