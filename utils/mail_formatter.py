'''Module which contains the function that formats the fetched jobs as a string for the mail_sender.'''

def mail_format(jobs_list):
    formatted = [f'''The company {job[1]} has a position open for: {job[2]}. This was opened
                 on {job[3]} and the deadline is {job[4]}. Link for more details: {job[5]} \n'''
                 for job in jobs_list]
    return ''.join(formatted)

