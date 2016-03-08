import json
from jsonschema import validate,Draft3Validator


def schemaValidator():
	
	schema_read=open("evaluationSchema.JSON").read()
	schema=json.loads(schema_read)
	Draft3Validator.check_schema(schema)
	
	data_read=open('evaluation.JSON').read()
	act_data=json.loads(data_read)
	if validate(act_data,schema):
		return True
	return False





