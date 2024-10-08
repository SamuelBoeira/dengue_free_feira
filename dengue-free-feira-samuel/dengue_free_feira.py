#Autor: Samuel Boeira Dantas
#Componenete curricula: 2024.1 EXA854 - MI - ALGORITMOS (TP04)
#Concluído em: 01/06/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum techo de código 
#de outro colega ou de outro autor, tais como provindos de livros e apostilas, e páginas de documentos
#eletrônicos da internet. Qualquer trecho de código de outra autoria que não a minha está destacado com
#uma citação para o autor e a fonte do código, e estou ciente que esses techaos não serão considerados 
#para fins de avaliação.

import csv
from datetime import datetime, timedelta
from tabulate import tabulate

def csv_reader():  #função que lê todas as informações do arquivo e imprime na tela em forma de tabela
    with open('UEFS\PBL Tiago Amador 24.1\dengue-free-feira-samuel\entrada.csv', 'r', encoding='utf8') as entry_csv:
        reader = csv.DictReader(entry_csv)
        table = tabulate(reader, headers="keys", tablefmt="grid")
        print(table)


def csv_neighborhood_date(option): #função conjunto, usuário pode escolher entre data ou bairro específico, essa def irá identificar qual é.
    with open('./entrada.csv', 'r', encoding='utf8') as entry_csv:
        reader = csv.DictReader(entry_csv)
        openaslist = list(reader)
        filtro = []
        if see_table == 2:
            for row in openaslist:
                if row["Data"] == option:
                    filtro.append(row)
            if filtro: print(tabulate(filtro, headers='keys', tablefmt="grid"))
            else: print("Data não disponível! Selecione uma data válido.")
        elif see_table == 3: 
            for row in openaslist:
                if row["Bairros"] == option:
                    filtro.append(row)
            if filtro: print(tabulate(filtro, headers="keys", tablefmt="grid"))
            else: print("Bairro não disponível! Selecione um bairro válido.")


def plus_date(): #função que adiciona um dia a data anterior para acrescentar novos dados
    with open('./entrada.csv', 'r', encoding='utf8') as entry_csv:
        lines = list(csv.reader(entry_csv))
        last_date = lines[-1][0] #pega a última data dentro do arquivo .csv em formato de texto
        last_date = datetime.strptime(last_date, "%d/%m/%Y") #transforma de texto em data
        new_date = last_date + timedelta(days=1) #soma o último dia mais um
        new_date_update = new_date.date().strftime("%d/%m/%Y") #.date() para mostrar apenas a data, sem horas, e .strftime
        #para alterar para visualização brasileira de datas
        return new_date_update 


def compare_dates(date1, date2):#duas listas de dicionários com as informações da data1 e data2.            
    date1_suspects = []
    date1_negative = []
    date1_positive = []
    date2_suspects = []
    date2_negative = []
    date2_positive = []
    #adiciona os valores de cada data separadamente 
    for line in dates_cases:
        if line['Data'] == date1:
            date1_suspects.append(line['Casos Suspeitos'])
            date1_negative.append(line['Casos Negativos'])
            date1_positive.append(line['Casos Confirmados'])
        if line['Data'] == date2:
            date2_suspects.append(line['Casos Suspeitos'])
            date2_negative.append(line['Casos Negativos'])
            date2_positive.append(line['Casos Confirmados'])
    #transforma tudo em inteiro
    suspects_int1 = list(map(int, date1_suspects))
    negative_int1 = list(map(int, date1_negative))
    positive_int1 = list(map(int, date1_positive))
    suspects_int2 = list(map(int, date2_suspects))
    negative_int2 = list(map(int, date2_negative))
    positive_int2 = list(map(int, date2_positive))
    #soma os valores armazenados dentro das listas para fazer os cálculos de comparação
    totaldate1_suspects = sum(suspects_int1)
    totaldate1_negative = sum(negative_int1)
    totaldate1_positive = sum(positive_int1)
    totaldate2_suspects = sum(suspects_int2)
    totaldate2_negative = sum(negative_int2)
    totaldate2_positive = sum(positive_int2)
    #porcentagem sendo o valor menor dividido pelo maior e multiplicado por 100 para adiquirir porcentagem, o -100 é para saber quanto de aumento
    percentual_suspects = ((totaldate1_suspects/totaldate2_suspects) * 100) - 100
    percentual_negative = ((totaldate1_negative/totaldate2_negative) * 100) - 100
    percentual_positive = ((totaldate1_positive/totaldate2_positive) * 100) - 100
    table = [[delta.days, percentual_suspects, percentual_negative, percentual_positive]]
    if totaldate1_suspects - totaldate2_suspects < 0: print(
f'''Se passaram {delta.days} dias e o aumento de suspeitos foi de {totaldate2_suspects - totaldate1_suspects} ou {100 - ((totaldate1_suspects/totaldate2_suspects) * 100):.2f}%,
o aumento de negativos foi de {totaldate2_negative - totaldate1_negative} ou {100 - ((totaldate1_negative/totaldate2_negative) * 100):.2f}%, já o aumento de casos
confirmados foi de {totaldate2_positive - totaldate1_positive} ou {100 - ((totaldate1_positive/totaldate2_positive) * 100):.2f}%.''')
    
    elif totaldate1_suspects - totaldate2_suspects > 0: print(
f'''Se passaram {delta.days} dias e o decréscimo de suspeitos foi de {totaldate1_suspects - totaldate2_suspects} ou {100 - ((totaldate1_suspects/totaldate2_suspects) * 100):.2f}%,
o aumento de negativos foi de {totaldate2_negative - totaldate1_negative} ou {100 - ((totaldate1_negative/totaldate2_negative) * 100):.2f}%, já o aumento de casos
confirmados foi de {totaldate2_positive - totaldate1_positive} ou {100 - ((totaldate1_positive/totaldate2_positive) * 100):.2f}%.''')       


def notified_percentual(): #função para encontrar o percentual de casos suspeitos, positivos e negativos da última data.
    with open('./entrada.csv', 'r', encoding='utf8') as entry_csv:
        reader = list(csv.reader(entry_csv))
        last_date = reader[-1][0]
        neighborhood = list()
        neighborhood_suspects = []
        neighborhood_negatives = []
        neighborhood_positives = []
        for line in reversed(reader):
            if line[0] == last_date: #condicional para adicionar apenas dados da última data
                all_neighborhood = line
                neighborhood.append(all_neighborhood)
            else: break
        for line in reversed(neighborhood):
            neighborhood_suspects.append(line[3])
            neighborhood_negatives.append(line[4])
            neighborhood_positives.append(line[5])
        suspects_int = list(map(int, neighborhood_suspects))
        negative_int = list(map(int, neighborhood_negatives))
        positive_int = list(map(int, neighborhood_positives))
        total_suspects = sum(suspects_int)
        total_negatives = sum(negative_int)
        total_positive = sum(positive_int)
        notifieds = total_negatives + total_positive + total_suspects #notificados são todos os dados(suspeitos, confirmados e negativados) somados
        percentual_suspects = (total_suspects/notifieds) * 100
        percentual_negatives = (total_negatives/notifieds) * 100
        percentual_positives = (total_positive/notifieds) * 100
        print(f'''O total de casos notificados até o dia {last_date} foi {notifieds}, sendo que {percentual_suspects:.2f}% foram casos 
suspeitos, {percentual_negatives:.2f}% foram casos negativos e {percentual_positives:.2f}% foram casos confirmados.''')

        
def csv_writer(new_date): #função que incialmente apenas armazena os dados da última data e logo após fazer os cálculos com as novas informações
    #inseridas ela abre o arquivo como modo de adição e transcreve os resultados de forma organizada.
    with open('./entrada.csv', 'r', encoding='utf8') as entry_csv:
        reader = list(csv.DictReader(entry_csv))
        #Uso de dicionários para poder armazenar cada valor de casos do dia anterior e poder fazer os cálculos posteriormente
        previus_suspects = {}
        previus_negative = {} 
        previus_positive = {}
        previus_district = list()
        recent_cases = {}
        for line in reversed(reader[1:]): #função para ler a lista 'reader' de trás para frente
            recent_district = line['Bairros']
            if recent_district in previus_district:
                break
            previus_district.append(recent_district)
            recent_cases[recent_district] = line
        
        for district, line in recent_cases.items():
            previus_suspects[district] = int(line['Casos Suspeitos'])
            previus_negative[district] = int(line['Casos Negativos'])
            previus_positive[district] = int(line['Casos Confirmados'])
        
        new_cases = {}
        for district in reversed(previus_district):
            new_suspects = int(input(f"Quantos NOVOS casos suspeitos para {district}? "))
            new_negative = int(input(f"Quantos NOVOS casos negativos {district}? "))
            new_positive = int(input(f"Quantos NOVOS casos positivos {district}? "))
            if new_negative + new_positive > previus_suspects[district]:
                print("Número de novos casos positivos e negativos maior que o de suspeitos do dia anterior! Adicione novamente.")
                break #verificação para caso o número de positivos e negativos recentes seja maior que o dia anterior 
            else: new_cases[district] = (new_suspects, new_negative, new_positive)
        
    with open('entrada.csv', 'a', encoding='utf8', newline='') as entry_csv: #aqui abre o arquivo como modo de adição
        fields = ['Data','Bairros','Habitantes','Casos Suspeitos','Casos Negativos','Casos Confirmados']
        writer = csv.DictWriter(entry_csv, fieldnames=fields)
        new_date = plus_date()
        for district in reversed(previus_district):
            recent_suspects = (previus_suspects[district] + new_cases[district][0]) - (new_cases[district][1] + new_cases[district][2])
            recent_negative = previus_negative[district] + new_cases[district][1]
            recent_positives = previus_positive[district] + new_cases[district][2]
            line = {
'Data': new_date, 'Bairros': district, 'Habitantes': recent_cases[district]['Habitantes'], 'Casos Suspeitos': recent_suspects, 
'Casos Negativos': recent_negative,'Casos Confirmados': recent_positives} #separa como ele deve transcrever os dados obtidos no arquivo csv
            writer.writerow(line)


print("Bem vindos ao programa Dengue Free Feira, o programa de vigilância sanitária de Feira de Santana!")
validate = False
while not validate:
    print(" ")
    menu = int(input('''Escolha uma opção para continuar: 
[1] Informações sobre a dengue.
[2] Ler ou armazenar dados.
[3] Encerrar programa. 
Opção: '''))
    if menu == 1:
        print(" ")
        print('''> O que é a dengue?
Caracteriza-se como uma doença infecciosa febril aguda, que dependendo do vírus
transmitido, se já ocorreu infecção anterior pelo vírus da dengue ou indivíduo 
já possua doenças crônicas (diabete, asma, anemia) a dengue pode ser benigna ou 
grave.

> Qual o microrganismo envolvido?
Pertencente da família do flavivírus, o vírus da dengue é classificado no meio 
científico como um arbovírus (vírus transmitido por picada), os quais são trans-
mitidos pelos mosquitos Aedes Aegypti e são conhecidos os sorotipos: 1, 2, 3 e 4.
Só pode ser transmitido pela picada da fêmea do mosquito Aedes aegypti e não há 
registro de transmissão pelo contato direto com um doente. 

> Quais os sintomas?
Podem ser apresentados sintomas como febre, dor de cabeça, dores pelo corpo, 
náuseas ou até mesmo nenhum dos anteriores. Caso note manchas vermelhas na pele,
sangramentos, dor abdominal intensa e contínua e vômitos persistem-tes é um pos-
sível sinal para dengue hemorrágica, que é um quadro grave e precisa de ajuda
médica imediata.

> Como tratar e previnir?
Inicalmente é de suma importância que medicamentos à base de ácido acetil sali-
cílico e antiinflamatórios, como aspirina e AAS, sejam evitados a todo custo, já
que eles podem aumentar o risco de hemorragia. Além disso, é importante o indi-
se manter altamente hidratado, seja por consumo oral ou venosa, fora isso todos
tratamentos devem ser indicados por médicos. Quanto à prevenção, é nescessário
o combate à água parada, sejam em pneus, poças, vasos de plantes... Já que esses
são os locais que o mosquito transmissor se desenvolve.
Fonte: bvsms.saude.gov.br/dengue-16''')

    if menu == 2:
        menu2 = int(input('''Deseja ler dados armazenados ou armazenar novos dados?
[1] Ler dados.
[2] Armazenar dados.
Opção: '''))
        if menu2 == 1:
            see_table = int(input('''Selecione a opção de leitura: 
[1] Leitura total.
[2] Por data.
[3] Por bairro.                                 
[4] Dados totais e estatísticos.
Opção: '''))
            if see_table == 1:
                csv_reader()
            if see_table == 2:
                data = str(input("Digite a data desejada para leitura(dd/mm/aaaa): "))
                csv_neighborhood_date(data)
            if see_table == 3:
                neighborhood = str(input("Digite o bairro desejado para leitura com a 1ª letra maiúscula e acentos: "))
                csv_neighborhood_date(neighborhood)
            if see_table == 4:
                see_estatistic_table = int(input('''Selecione a opção de leitura: 
[1] Comparar duas datas.
[2] Porcentagem total de casos notificados. (Última data)                                  
Opção: '''))
                if see_estatistic_table == 1:
                        with open('./entrada.csv', 'r', encoding='utf8') as entry_csv:
                            reader = list(csv.DictReader(entry_csv))
                            dates = list()
                            dates_cases = list()
                            for line in reader[0:]: #loop para armazenar todas as datas em uma lista
                                all_dates = line['Data']
                                dates.append(all_dates)
                                dates_cases.append(line)
                            validate_date = False
                            while not validate_date:
                                date1 = input("Escolha uma data (com exceção da mais recente) para comparação(dd/mm/aaaa): ")
                                date2 = input("Escolha uma data mais recente para comparação(dd/mm/aaaa): ")
                                date_datetime = datetime.strptime(date1, "%d/%m/%Y") 
                                #transforma ambas as datas em formato datetime
                                date_datetime2 = datetime.strptime(date2, "%d/%m/%Y")
                                delta = date_datetime2 - date_datetime
                                days_past = delta.days
                                if date1 and date2 in dates:       
                                    compare_dates(date1, date2)
                                    validate_date = True
                                else: print("Uma das datas não está dentro do arquivo! Por favor, digite novamente.")
                if see_estatistic_table == 2:
                    notified_percentual()
                    
        if menu2 == 2:
            plus_date()
            csv_writer(plus_date)
    if menu == 3: 
        validate = True

print("Obrigado por contribuir!")