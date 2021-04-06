# AutoComplete.py
def AutoComplete(repository, query):
    endPos = 1
    subquery = query[:endPos]
    while len(subquery) <= len(query):
        queryRes = []
        for item in repository:
            if item.startswith(subquery):
                queryRes.append(item)
        print(sorted(queryRes)[:3])
        endPos += 1
        if endPos == len(query):
            break
        else:
            subquery = query[:endPos]


repository = [
    "mobile",
    "mouse",
    "moneypot",
    "monitor",
    "mousepad",
    "matchstick",
    "mascara",
]
customerQuery = input("Enter the query: ")
print(customerQuery)
AutoComplete(repository, customerQuery)
