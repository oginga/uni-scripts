import json
from jsonschema import validate,Draft3Validator


def schemaValidator():
	'''
		validator
	'''
	
	schema_read=open("evaluationSchema.json").read()
	schema=json.loads(schema_read)
	print schema
	print "\n\n\n\n"
	#Draft3Validator.check_schema(schema)
	
	data_read=open('course_jsons/ComputerScience3_2.json').read()
	act_data=json.loads(data_read)
	print act_data
	units=act_data['units']
	for k,v in units.items():
		radios=units[k]['radios']
		print '\n\n\n'
		print radios

	if validate(act_data,schema):
		return True
	return False


def load_json():
	data_read=open('evaluation.json').read()
	act_data=json.loads(data_read)
	return act_data


if __name__ == "__main__":
	s=schemaValidator()
	print s




