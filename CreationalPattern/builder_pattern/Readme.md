# Builder Design Pattern
When an object required many parameters, especially optional ones, the constructor can become hard to use or maintain. This issue can lead to:

1. Long constructor parameter lists,
2. Difficulty in understanding which values are optional or required.
3. Lack of felxibility when it it comes to setting only some values.

For example, constructing an object with multile optional parameters without the Builder pattern can look like (i.e without_builder_pattern.py)