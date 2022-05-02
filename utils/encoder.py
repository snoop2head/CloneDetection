
class Encoder :
    def __init__(self, tokenizer, max_input_length: int) :
        self.tokenizer = tokenizer
        self.max_input_length = max_input_length
    
    def __call__(self, examples):
        model_inputs = self.tokenizer(examples['code1'], 
            max_length=self.max_input_length, 
            return_token_type_ids=False,
            truncation=True
        )

        code2_model_inputs = self.tokenizer(examples['code2'], 
            max_length=self.max_input_length, 
            return_token_type_ids=False,
            truncation=True
        )

        model_inputs['input_ids2'] = code2_model_inputs['input_ids']
        model_inputs['attention_mask2'] = code2_model_inputs['attention_mask']

        if 'similar' in examples :
            model_inputs['labels'] = examples['similar']
        return model_inputs