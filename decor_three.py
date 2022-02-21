# Каждый год ваша компания предоставляет различным
# государственным организациям финансовую отчетность.
# В зависимости от организации форматы отчетности разные. 
# Используя механизм декораторов, 
# решите вопрос отчетности для организаций

#Не смогла разобраться с условием задачи, переделать после.
#Программа не работает.

def accounting(func):
    def reporting(organization, *args):
        name_of_company = organization
        all_report = func(*args)
        return name_of_company, all_report
    return reporting

@accounting
def gov_org(organization, *args):
    print('Финансовая отчетность для организации', organization, 'представлена:', *args)
    return None

var_rep = ['прибыль', 2500, 'убыток', 1000]
gov_org(organization = 'Mycompany', *var_rep)

 