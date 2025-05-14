import os
from llama_index.llms.openai import OpenAI
from sqlalchemy import create_engine
from schema_engine import SchemaEngine

dashscope_llm = OpenAI(temperature=0.0, model="gpt-4.1", store=True)

db_path = './mimic_iv.sqlite'
db_abs_path = os.path.abspath(db_path)
db_engine = create_engine(f'sqlite:///{db_abs_path}')

comment_mode = 'generation'
schema_engine_instance = SchemaEngine(db_engine, llm=dashscope_llm, db_name='mimic_iv',
                                      comment_mode=comment_mode)
schema_engine_instance.fields_category()
schema_engine_instance.table_and_column_desc_generation(language='EN')
mschema = schema_engine_instance.mschema
mschema.save('./mimic_iv.json')
mschema_str = mschema.to_mschema()
print(mschema_str)