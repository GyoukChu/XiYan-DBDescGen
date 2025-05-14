from llama_index.core.prompts import PromptTemplate
from llama_index.core.prompts.prompt_type import PromptType

DEFAULT_IS_DATE_TIME_FIELD_TMPL = """You are now a data analyst. Given the relevant information of a column in a data table, please analyze whether this column belongs to a date-time type. Answer only "Yes" or "No".
A date-time type refers to a combination of one or more of year, month, day, hour, minute, and second. It requires that the month must be between 1-12, the day between 1-31, the hour between 0-23, and the minute and second between 0-59.

{field_info_str}
"""

DEFAULT_IS_DATE_TIME_FIELD_PROMPT = PromptTemplate(
    DEFAULT_IS_DATE_TIME_FIELD_TMPL,
    prompt_type=PromptType.CUSTOM,
)

# Minimum granularity of date-time type fields 
DEFAULT_DATE_TIME_MIN_GRAN_TMPL = """You are now a data analyst. Given a field in a data table, it is known that the meaning of this field is related to date and time. Please infer the minimum granularity of this field based on its composition format and data examples.
Explanation: The minimum granularity of a date-time field refers to the smallest time unit to which the field can be precise.

The following are common time units:
YEAR: The smallest time unit is one year, e.g., 2024
MONTH: The month of a certain year, there are 12 months in a year, Month takes values between 1-12, e.g., 2024-12
DAY: The day of a certain month, a month has at most 31 days, so Day takes values between 1-31, e.g., 2024-12-31
WEEK: Natural week, generally the week number in a year, a year contains 52 weeks and a few more days, Week is usually between 0-53, e.g., 2024-34
QUARTER: The quarter of a certain year, there are four quarters in a year, Quarter usually takes values between 1-4
HOUR: The hour of a certain day, there are 24 hours in a day, Hour is between 0-23
MINUTE: The minute of a certain hour, there are 60 minutes in an hour, Minute is between 0-59
SECOND: The second of a certain minute, there are 60 seconds in a minute, Second is between 0-59
MILLISECOND: Millisecond
MICROSECOND: Microsecond
OTHER: Other time units not listed above, such as half a year, a quarter of an hour, etc.

Directly provide the name of the minimum time unit.

The following examples are for your reference:
【Field Information】
Field Name: dt
Data Type: DOUBLE
Value Examples: [202412.0, 202301.0 202411.0, 202201.0, 202308.0, 202110.0, 202211.0]
Minimum Time Unit: MONTH

【Field Information】
Field Name: dt
Data Type: TEXT
Value Examples: ['2022-12', '2022-14', '2021-40', '2021-37', '2021-01', '2021-32', '2023-04', '2023-37']
Minimum Time Unit: WEEK

【Field Information】
Field Name: dt
Data Type: TEXT
Value Examples: ['12:30:30', '23:45:23', '01:23:12', '12:12:12', '14:34:31', '18:43:01', '22:13:21']
Minimum Time Unit: SECOND

Please refer to the examples above to infer the minimum time unit of the following field. Directly provide the name of the minimum time unit.
【Field Information】
{field_info_str}
Minimum Time Unit: """

DEFAULT_DATE_TIME_MIN_GRAN_PROMPT = PromptTemplate(
    DEFAULT_DATE_TIME_MIN_GRAN_TMPL,
    prompt_type=PromptType.CUSTOM,
)


DEFAULT_STRING_CATEGORY_FIELD_TMPL = '''You are now a data analyst. Given the relevant information of a column in a data table, please analyze whether this column is of enum type, code type, or text type. Answer only "enum", "code", or "text".

enum: Has enumeration characteristics: field values are relatively fixed, concentrated within a predefined finite set, usually short in length, with a relatively fixed composition pattern, generally used for status, type, and other fields.
code: A code with specific meaning, the composition of a code usually follows certain rules or standards, such as user ID, ID card number, etc.
text: Free text, usually used for description or explanation, not limited by length or form, the content can be any form of text.

{field_info_str}
'''

DEFAULT_STRING_CATEGORY_FIELD_PROMPT = PromptTemplate(
    DEFAULT_STRING_CATEGORY_FIELD_TMPL,
    prompt_type=PromptType.CUSTOM,
)

DEFAULT_NUMBER_CATEGORY_FIELD_TMPL = """You are now a data analyst. Given the relevant information of a column in a data table, please analyze whether this column is of enum type, code type, or measure type. Answer only "enum", "code", or "measure".

enum: Enumeration type, values are limited to a predefined finite set, usually short in length, generally used for status, type, and other fields.
code: A code with specific meaning, the composition of a code usually follows certain rules or standards, such as user ID, ID card number, etc.
measure: Metric, measure, can be used for calculations and aggregations, such as calculating average, maximum value, etc.

{field_info_str}
"""

DEFAULT_NUMBER_CATEGORY_FIELD_PROMPT = PromptTemplate(
    DEFAULT_NUMBER_CATEGORY_FIELD_TMPL,
    prompt_type=PromptType.CUSTOM,
)

DEFAULT_UNKNOWN_CATEGORY_FIELD_TMPL = """You are now a data analyst. Given the relevant information of a column in a data table, please analyze whether this column is of enum type, measure type, code type, or text type. Answer only "enum", "measure", "code", or "text".

enum: Enumeration type, values are limited to a predefined finite set, usually short in length, generally used for status, type, and other fields.
code: A code with specific meaning, the composition of a code usually follows certain rules or standards, such as user ID, ID card number, etc.
text: Free text, usually used for description or explanation, not limited by length, the content can be any form of text.
measure: Metric, measure, can be used for calculations and aggregations, such as calculating average, maximum value, etc.

{field_info_str}
"""

DEFAULT_UNKNOWN_FIELD_PROMPT = PromptTemplate(
    DEFAULT_UNKNOWN_CATEGORY_FIELD_TMPL,
    prompt_type=PromptType.CUSTOM,
)

DEFAULT_COLUMN_DESC_GEN_CHINESE_TMPL = '''You are now a data analyst. You are given the field information of a data table and some data samples as follows:

{table_mschema}

【SQL】
{sql}
【Examples】
{sql_res}

Below is the detailed information for the field "{field_name}" in this table:
{field_info_str}

The following information is for your reference:
{supp_info}

Now, please carefully read and understand the above content and data, and add a Chinese name for the field "{field_name}", with the following requirements:
1. The Chinese name should be as concise and clear as possible, accurately describing the business semantics represented by the field, without deviating from the original field description.
2. The length of the Chinese field name should not exceed 20 characters.
3. Output in JSON format:
```json
{"chinese_name": ""}
```
'''

DEFAULT_COLUMN_DESC_GEN_CHINESE_PROMPT = PromptTemplate(
    DEFAULT_COLUMN_DESC_GEN_CHINESE_TMPL,
    prompt_type=PromptType.CUSTOM,
)

DEFAULT_COLUMN_DESC_GEN_ENGLISH_TMPL = '''You are now a data analyst. You are given the field information of a data table and some data samples as follows:

{table_mschema}

【SQL】
{sql}
【Examples】
{sql_res}

Below is the detailed information for the field "{field_name}" in this table:
{field_info_str}

The following information is for your reference:
{supp_info}

Now, please carefully read and understand the above content and data, and add an English description for the field "{field_name}", with the following requirements:
1. The English description should be as concise and clear as possible, accurately describing the business semantics represented by the field, without deviating from the original field description.
2. The total output length should not exceed 20 words.
3. Output in JSON format:
```json
{"english_desc": ""}
```
'''

DEFAULT_COLUMN_DESC_GEN_ENGLISH_PROMPT = PromptTemplate(
    DEFAULT_COLUMN_DESC_GEN_ENGLISH_TMPL,
    prompt_type=PromptType.CUSTOM,
)


DEFAULT_UNDERSTAND_DATABASE_TMPL = '''You are now a data analyst. You are given the schema of a database as follows:

{db_mschema}

Please carefully read the above information and analyze at the database level what domain and what data this database primarily stores. Provide a summary; no need to analyze each table individually.
'''

DEFAULT_UNDERSTAND_DATABASE_PROMPT = PromptTemplate(
    DEFAULT_UNDERSTAND_DATABASE_TMPL,
    prompt_type=PromptType.CUSTOM,
)

DEFAULT_GET_DOMAIN_KNOWLEDGE_TMPL = '''There is such a database, with basic information as follows:
{db_info}

Based on your acquired knowledge, what are the common dimensions and metrics that people in this domain are typically concerned with?
'''

DEFAULT_GET_DOMAIN_KNOWLEDGE_PROMPT = PromptTemplate(
    DEFAULT_GET_DOMAIN_KNOWLEDGE_TMPL,
    prompt_type=PromptType.CUSTOM,
)

DEFAULT_UNDERSTAND_FIELDS_BY_CATEGORY_TMPL = '''You are now a data analyst. You are given the basic information of a dataset:

【Database Information】
{db_info}

Among them, the field information and data samples for the data table "{table_name}" are as follows:
{table_mschema}

【SQL】
{sql}
【Examples】
{sql_res}

Please carefully read and understand this data table. Given that the fields {fields} in the table are all {category} fields, please analyze the relationships and differences between these fields.
'''

DEFAULT_UNDERSTAND_FIELDS_BY_CATEGORY_PROMPT = PromptTemplate(
    DEFAULT_UNDERSTAND_FIELDS_BY_CATEGORY_TMPL,
    prompt_type=PromptType.CUSTOM,
)

DEFAULT_TABLE_DESC_GEN_CHINESE_TMPL = '''You are now a data analyst. You are given the field information of a data table as follows:

{table_mschema}

Below are some data samples:
【SQL】
{sql}
【Examples】
{sql_res}

Now, please carefully read and understand the above content and data, and generate a Chinese table description for this data table, with the following requirements:
1. Explain what metric data the table stores, and on what dimensions (including time dimensions and other dimensions).
2. Control the character count to within 100 characters.
3. Output the answer in JSON format.

```json
{"table_desc": ""}
```
'''

DEFAULT_TABLE_DESC_GEN_CHINESE_PROMPT = PromptTemplate(
    DEFAULT_TABLE_DESC_GEN_CHINESE_TMPL,
    prompt_type=PromptType.CUSTOM,
)

DEFAULT_TABLE_DESC_GEN_ENGLISH_TMPL = '''You are now a data analyst. You are given the field information of a data table as follows:

{table_mschema}

Below are some data samples:
【SQL】
{sql}
【Examples】
{sql_res}

Now, please carefully read and understand the above content and data, and generate an English table description for this data table, with the following requirements:
1. Explain what metric data the table stores, and on what dimensions (including time dimensions and other dimensions).
2. The length should not exceed 100 words.
3. Output the answer in JSON format.

```json
{"table_desc": ""}
```
'''

DEFAULT_TABLE_DESC_GEN_ENGLISH_PROMPT = PromptTemplate(
    DEFAULT_TABLE_DESC_GEN_ENGLISH_TMPL,
    prompt_type=PromptType.CUSTOM,
)

DEFAULT_SQL_GEN_TMPL = '''You are now a {dialect} data analyst. You are given the schema information of a database as follows:

【Database Schema】
{db_mschema}

【User Question】
{question}
【Reference Information】
{evidence}

Please carefully read and understand this database. Based on the user's question and the hints from the reference information, generate an executable SQL statement to answer the user's question. Enclose the generated SQL with ```sql and ```.
'''

DEFAULT_SQL_GEN_PROMPT = PromptTemplate(
    DEFAULT_SQL_GEN_TMPL,
    prompt_type=PromptType.CUSTOM,
)

