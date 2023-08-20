import parsing_data
import LLMmodel

def find_user_id(seq):
    import re
    # print(f"{seq['generated_text']}")
    start_index = seq.find("user_id:") + len("user_id:")
    # Extract the user_id
    user_id = seq[start_index:].split()[0]
    user_id_match = re.search(r'^(\d+)[;:\s]', user_id)
    if user_id_match:
        user_id = user_id_match.group(1)
        return user_id


def reduced_req_response(response):
    import re
    # Define regular expressions for "breach:" and "fix:" lines
    breach_pattern = re.compile(r'^breach:\s*(.*?)$', re.MULTILINE)
    fix_pattern = re.compile(r'^fix:\s*(.*?)$', re.MULTILINE)

    # Find the first occurrences of "breach:" and "fix:" lines
    breach_match = breach_pattern.search(response)
    fix_match = fix_pattern.search(response)
    return f"breach: {breach_match}\nfix: {fix_match}\n"


def identify_breaches_and_report(logs, ruleset):
    breach_reports = []
    
    for i, user_log in enumerate(logs, start=1):
        breach_response = ""
        breach_found = False
        concat_log = ', '.join(user_log)
        
        if logs[0][0] == "user_id":
            user_id = user_log[0]
        else:
            idprompt = f"Tell me the user_id for the log: {concat_log} \nin the following format: \nuser_id:"
            user_id = find_user_id(LLMmodel.generate_response(idprompt, len(idprompt) + 25))

        for rule in ruleset:
            prompt = f"Log: {concat_log}\nRule: {rule}\nDoes the log follow the rule? If not, provide an explanation or suggest a fix as following\nbreach:\nfix:\n"
            response = LLMmodel.generate_response(prompt, len(prompt) + 75)
            
            if "no_breach" not in response.lower():
                index = response.index("### Solution:") + len("### Solution:")
                response = response[index:]

                breach_response += reduced_req_response(response)
                breach_found = True
        
        if breach_found:
            #appends log_line, user_id, fixes
            breach_reports.append((i, user_id, breach_response))

    
    return breach_reports



def main():

    log_file_path = input("Enter the path to the log file (PDF, CSV, or TXT): ")
    ruleset_file_path = input("Enter the path to the ruleset file (PDF, CSV, TXT, or JSON): ")

    temp = parsing_data.parse(log_file_path, ruleset_file_path)

    # log_data = temp[0]
    # ruleset_data = temp[1]

    breaches = identify_breaches_and_report(temp[0], temp[1])
    
    if breaches and breaches[0]:
        with open("comp/breaches.txt", "w") as f:
            f.write("Breaches detected:\n")
            for breach in breaches:
                if breach:
                    f.write(f"Log number: {breach[0]}, User_id: {breach[1]}\nDetails:\n{breach[2]}\n\n")
        print("Breaches saved in 'breaches.txt' file.")
    else:
        print("No breaches detected.")


if __name__ == "__main__":
    main()