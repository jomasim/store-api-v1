class Request():

    def __init__(self,request,schema):
        self.request=request
        self.schema=schema

    ''' this method accepts raw request and request rules '''
  
    def validate(self):
        ''' all request rules '''
        all_rules=self.get_request_rules()
        all_errors={}
        ''' get all errors from request  '''
        for field_rules in all_rules:
            ''' get all errors for a single field '''
            field_error=self.validate_field(field_rules,all_rules[field_rules])
            if field_error:
                all_errors[field_rules]=field_error
            
        if all_errors:
                return {"errors":all_errors}
        return None
        


    ''' this method gets all field rules from filed rules string '''
    @staticmethod
    def get_field_rules(rules_string):
        return rules_string.split('|')

    ''' gets all request validation rules for each field '''

    def get_request_rules(self):
        fields=self.schema
        request_rules={}
        for field in fields:
            request_rules[field]=Request.get_field_rules(fields[field])
        return request_rules
    
    def __min(self,arg):
        pass

    def __max(self,arg):
        pass

    def __email(self,arg):
        pass
    def __isRequired(self,arg):
        pass
    def isString(self,arg):
        if not isinstance(arg,str):
            return "should be a string"
        return True
    def isInt(self, arg):
        if not isinstance(arg,int):
            return "should be a string"
        return True
    def isEmpty(self,arg):
        if arg == "":
            return True

    def validate_field(self,field,field_rules):
        value=self.get_value(field)
        field_errors=[]
      
        if 'required' in field_rules and value==None or self.isEmpty(value):
            field_errors.append(field + " is required")
        elif 'email' in field_rules:
            pass
        elif 'min'in field_rules:
            pass
        elif 'max' in field_rules:
            pass
        return field_errors
           
    def get_value(self,field_key):
        ''' get field value from request using key '''
        if field_key in self.request:
            return self.request[field_key]
        return None
        


            


