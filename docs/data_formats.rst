Data Formats
============



BasicTypes
----------


:description: Representation of fundamental data types: Strings, Numbers, and Booleans.


Parameters:

* string_val: String

* number_val: String

* boolean_val: String

* notes: String



.. list-table:: BasicTypes Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - string_val
     - number_val
     - boolean_val
     - notes
   * - JsonBasic
     - "Hello"
     - 42 or 3.14
     - true / false
     - Standard JSON types; strings must be double-quoted.
   * - XmlBasic
     - <tag>Hello</tag>
     - <tag>42</tag>
     - <tag>true</tag>
     - XML is text-based; types are typically inferred or defined by a schema (XSD).
   * - YamlBasic
     - Hello or 'Hello' or "Hello"
     - 42 or 3.14
     - true / false (or yes/no, on/off in YAML 1.1)
     - YAML supports plain, single-quoted, and double-quoted strings.
   * - TomlBasic
     - "Hello"
     - 42 or 3.14
     - true / false
     - TOML is strictly typed; strings must be double-quoted.
   * - CsvBasic
     - Hello or "Hello"
     - 42 or 3.14
     - true / false
     - CSV values are typically plain text; quoting is used for values containing delimiters or newlines.



Collection
----------


:description: Ordered sequence of elements (Arrays, Lists, or Sequences).


Parameters:

* elements: String

* syntax: String

* notes: String



.. list-table:: Collection Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - elements
     - syntax
     - notes
   * - JsonCollection
     - Any JSON value
     - ``[1, "two", true]``
     - Elements are comma-separated and enclosed in square brackets.
   * - XmlCollection
     - Repeated child elements
     - | ``<list>``
       | ``  <item>1</item>``
       | ``  <item>2</item>``
       | ``</list>``
     - Collections are typically represented by repeating elements under a parent.
   * - YamlCollection
     - Any YAML value
     - | ``- 1``
       | ``- two``
       | ``- true``
     - Uses a dash followed by a space for each element.
   * - TomlCollection
     - Any TOML value
     - ``[1, 2, 3]``
     - Arrays can contain values of different types since TOML 1.0.0.
   * - CsvCollection
     - Comma-separated values
     - ``1,two,true``
     - A single row represents a collection of fields.



Mapping
-------


:description: Unordered collection of key-value pairs (Objects, Maps, or Dictionaries).


Parameters:

* entries: String

* syntax: String

* notes: String



.. list-table:: Mapping Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - entries
     - syntax
     - notes
   * - JsonMapping
     - Key-value pairs
     - ``{"key": "value", "num": 42}``
     - Keys must be double-quoted strings.
   * - XmlMapping
     - Child elements or attributes
     - | ``<object>``
       | ``  <key>value</key>``
       | ``  <num>42</num>``
       | ``</object>``
     - Mappings are represented as nested elements.
   * - YamlMapping
     - Key-value pairs
     - | ``key: value``
       | ``num: 42``
     - Uses a colon followed by a space to separate key and value.
   * - TomlMapping
     - Key-value pairs
     - | ``key = "value"``
       | ``num = 42``
     - Top-level or grouped using [headers].
   * - CsvMapping
     - Header to field mapping
     - | ``Name,Age``
       | ``Alice,30``
     - Mappings are established by associating header names with column values.



Metadata
--------


:description: Way to attach metadata or attributes to data elements.


Parameters:

* syntax: String

* notes: String



.. list-table:: Metadata Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - syntax
     - notes
   * - JsonMetadata
     - N/A
     - JSON does not support metadata or attributes on elements; often simulated using underscore-prefixed keys (e.g., "_metadata": { ... }).
   * - XmlMetadata
     - ``<element attr="value">Content</element>``
     - XML has native support for attributes on elements.
   * - YamlMetadata
     - ``!!str "value" or !custom { key: val }``
     - YAML supports tags to specify types or attach metadata to nodes.
   * - TomlMetadata
     - N/A
     - TOML does not support per-element metadata, though it uses headers for grouping.
   * - CsvMetadata
     - N/A
     - Standard CSV (RFC 4180) does not support metadata or attributes.



Comment
-------


:description: Way to add non-executable explanatory text to the data.


Parameters:

* single_line: String

* multi_line: String

* notes: String



.. list-table:: Comment Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - single_line
     - multi_line
     - notes
   * - JsonComment
     - N/A
     - N/A
     - JSON does not natively support comments.
   * - XmlComment
     - <!-- comment -->
     - | <!--
       |   line 1
       |   line 2
       | -->
     - XML uses the same syntax for single and multi-line comments.
   * - YamlComment
     - # comment
     - | # line 1
       | # line 2
     - YAML only supports single-line comments starting with #.
   * - TomlComment
     - # comment
     - | # line 1
       | # line 2
     - TOML only supports single-line comments starting with #.
   * - CsvComment
     - N/A
     - N/A
     - Standard CSV does not natively support comments; some variations use #.



SchemaLink
----------


:description: Linking a data file to a schema for validation (e.g., JSON Schema, XSD).


Parameters:

* syntax: String

* notes: String



.. list-table:: SchemaLink Comparison
   :widths: auto
   :header-rows: 1

   * - Instance
     - syntax
     - notes
   * - JsonSchemaLink
     - ``"\$schema": "http://json-schema.org/draft-07/schema#"``
     - JSON uses the \$schema keyword to point to a JSON Schema file.
   * - XmlSchemaLink
     - | ``<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"``
       | ``      xsi:schemaLocation="http://example.com schema.xsd">``
     - XML uses the xsi:schemaLocation attribute to link to an XSD.
   * - YamlSchemaLink
     - ``# yaml-language-server: \$schema=<url_or_path>``
     - YAML often relies on editor-specific comments (like VS Code's language server) for schema linking.
   * - TomlSchemaLink
     - N/A
     - TOML does not have a native or widely standardized way to link to a schema within the file.
   * - CsvSchemaLink
     - N/A
     - CSV does not have a native schema linking mechanism; often defined in a sidecar file (e.g., CSVW metadata).