from typing import List


def numUniqueEmails(emails: List[str]) -> int:
    
    uniques = []
    
    for m in emails:
        local, domain = m.split('@')
        local = local.replace('.','')
        for i, char in enumerate(local):
            if char == '+':
                local = local[:i]
                break
        if local + '@' + domain not in uniques:
            uniques.append(local + '@' + domain)
    
    print(uniques)
    return len(uniques)

'''
Time: O(n*k) where k is the average length of emails
Space: O(n)
'''