## Core OOP Concepts You Can Use in ETL

1. **Classes & Objects**

   * Each major component of your ETL can be represented as a class.
   * Example: `Extract`, `Transform`, `Load`.

2. **Inheritance**

   * Create base classes with common behavior and extend them for specific cases.
   * Example: A generic `Extractor` class, with `MySQLExtractor` and `S3Extractor` inheriting from it.

3. **Encapsulation**

   * Keep internal logic private (`_method` or `__method`) and expose only public methods.
   * Example: A `Transform` class can expose a `run()` method while keeping internal functions hidden.

4. **Polymorphism**

   * Use the same interface for different implementations.
   * Example: `extract()` method can behave differently depending on whether it reads from SQL, CSV, or API.

5. **Composition**

   * Combine multiple classes into a pipeline.
   * Example: `Pipeline` class that takes `Extractor`, `Transformer`, and `Loader` objects.


## Example ETL Structure Using OOP

```python
# Base class for extraction
class Extractor:
    def extract(self):
        raise NotImplementedError("Extractor must implement extract method")

# Specific extractor for MySQL
class MySQLExtractor(Extractor):
    def __init__(self, connection, query):
        self.connection = connection
        self.query = query
    
    def extract(self):
        print(f"Extracting data using query: {self.query}")
        # actual code to fetch from MySQL
        return [{"id": 1, "name": "Alice"}]

# Base class for transformation
class Transformer:
    def transform(self, data):
        raise NotImplementedError("Transformer must implement transform method")

# Simple transformer
class UpperCaseTransformer(Transformer):
    def transform(self, data):
        for row in data:
            row["name"] = row["name"].upper()
        return data

# Base class for loading
class Loader:
    def load(self, data):
        raise NotImplementedError("Loader must implement load method")

# Loader to print data
class PrintLoader(Loader):
    def load(self, data):
        print("Loading data:")
        for row in data:
            print(row)

# Pipeline class
class ETLPipeline:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        data = self.extractor.extract()
        data = self.transformer.transform(data)
        self.loader.load(data)

# Usage
extractor = MySQLExtractor(connection="my_conn", query="SELECT * FROM users")
transformer = UpperCaseTransformer()
loader = PrintLoader()

pipeline = ETLPipeline(extractor, transformer, loader)
pipeline.run()
```

**Output:**

```
Extracting data using query: SELECT * FROM users
Loading data:
{'id': 1, 'name': 'ALICE'}
```


## Why OOP Helps in ETL

| Concept           | Benefit in ETL                                  |
| ----------------- | ----------------------------------------------- |
| Classes & Objects | Modularize each step of ETL                     |
| Inheritance       | Reuse common logic (e.g., different extractors) |
| Polymorphism      | Swap implementations easily (CSV, API, SQL)     |
| Encapsulation     | Hide internal logic; reduce errors              |
| Composition       | Build flexible, dynamic pipelines               |