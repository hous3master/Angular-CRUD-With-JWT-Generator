# Angular Frontend Generator
Python CRUD frontend generator to speed up development.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Node.js
- Angular CLI
- A Spring backend secured with JWT tokens


This guide will help you understand how to use the `entities` data structure in this project.

### Entities

In this project, we use a data structure called `entities` to represent different types of objects. Each entity has a name and a set of attributes. Here's the general format:

```python
entities = [
    {
        "entityName": "<Entity Name>",
        "attributes": [
            ["<Data Type>", "<Attribute Name>"],
            # Add more attributes as needed
        ],
    },
    # Add more entities as needed
]
```

### Instructions

1. **Entity Name**: Replace `<Entity Name>` with the name of your entity.
2. **Attributes**: For each attribute of an entity, replace `<Data Type>` with the data type of the attribute and `<Attribute Name>` with the name of the attribute.
3. **Multiple Attributes**: If an entity has more than one attribute, add more lines in the format `["<Data Type>", "<Attribute Name>"],`.
4. **Multiple Entities**: If you have more than one entity, add more blocks in the format:
    ```python
    {
        "entityName": "<Entity Name>",
        "attributes": [
            ["<Data Type>", "<Attribute Name>"],
            # Add more attributes as needed
        ],
    },
    ```
5. **Syntax**: Make sure to keep the commas `,` at the end of each attribute and entity block to avoid syntax errors.

That's it! You're now ready to use the `entities` data structure in your project. If you have any more questions, feel free to ask!
