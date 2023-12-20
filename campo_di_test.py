import re

def process_string(input_string):
    # Define a regular expression pattern for uppercase pattern + short text + semicolon
    pattern = r'([A-Z]+[A-Z0-9]*\s*);'

    def replace_function(match):
        # If the uppercase pattern is found, replace with the match; otherwise, keep the semicolon
        return match.group(1) + ';' if match.group(1) else match.group(0)

    # Use re.sub with a function to perform conditional replacement
    result_string = re.sub(pattern, replace_function, input_string)

    return result_string

# Example usage
input_string = "\nselect count(*) into v_cnt from taboanalisi where codicecampione = '#codicecampione#' and nomeanalisi like '%anGra%';\n\nif v_cnt > 0 then\n  -- SQLINES LICENSE FOR EVALUATION USE ONLY\n  select 0 ASABORT from dual;\nelse \n  -- SQLINES LICENSE FOR EVALUATION USE ONLY\n  select 1 AS ABORT from dual\n  ;\nend if;\nAPRIPOPUP PopUp_CurvaGranulometrica\n;\n"

result = process_string(input_string)
print("Original String:", input_string)
print("Processed String:", result)
