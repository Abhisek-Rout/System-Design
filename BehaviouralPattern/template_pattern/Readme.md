# Template Pattern
Consider a scenario where you have different data parsers (e.g CSV, XML and JSON). Each parser follows the same steps: *open file, parse data and close file*.

Without the Template pattern you might end up duplicating the common steps in each parser class.

# Problems in code without template pattern
1. Code duplication: The openFile() and closeFile() methods ae duplicated in both parsers.
2. Any changes to the common logic would require changes in very parser, violating the DRY (Don't Repeat Yourself) principle.

# Problem:
Diifferent parts of an algorithm may need to vary in subclasses, but the overall structure should remain consistent.

# Solution:
The template method pattern defines the skeleton of an algorithm in a base class and lets subclasses override specific steps.

# Structure
1. Abstract class: Defines the algorithm sskeleton.
2. Concrete Subclasses: Overrides specific steps of the algorithm.

