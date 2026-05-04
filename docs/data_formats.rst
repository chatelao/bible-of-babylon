

BasicTypes
==========


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
     - \"Hello\"
     - 42 or 3.14
     - true / false
     - Standard JSON types; strings must be double-quoted.
   * - XmlBasic
     - <tag>Hello</tag>
     - <tag>42</tag>
     - <tag>true</tag>
     - XML is text-based; types are typically inferred or defined by a schema (XSD).
   * - YamlBasic
     - Hello or 'Hello' or \"Hello\"
     - 42 or 3.14
     - true / false (or yes/no, on/off in YAML 1.1)
     - YAML supports plain, single-quoted, and double-quoted strings.
   * - TomlBasic
     - \"Hello\"
     - 42 or 3.14
     - true / false
     - TOML is strictly typed; strings must be double-quoted.