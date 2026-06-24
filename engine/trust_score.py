def calculate_trust_score(fact, logic, source, context):
    return (fact + logic + source + context) / 4