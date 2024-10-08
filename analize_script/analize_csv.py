import csv
import matplotlib.pyplot as plt

def leggi_csv(file_path):
    """
    Legge un file CSV e restituisce i dati sotto forma di lista di dizionari.
    
    :param file_path: Il percorso del file CSV da leggere.
    :return: Una lista di dizionari, dove ogni dizionario rappresenta una riga del CSV.
    """
    dati = []

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dati.append(row)
    
    return dati

# Esempio di utilizzo
file_path = '/home/sagemaker-user/DeepLearning_project/Results/test_15_07_ONLY_MEMO.csv'
dati = leggi_csv(file_path)

dati_before_MEMO = []
dati_after_MEMO = []
dati_after_MEMO_PLUS = []

for index, riga in enumerate(dati):
    if index != 0 and index != len(dati) - 1:
        split_name = riga['Class'].split('_')
        print(split_name)
        if split_name[1] == "before":
      
            data = eval(riga['Result_for_image'])
            tot_correct = 0
            for elem in data:
                tot_correct += elem[0]
            accuracy = (tot_correct/len(data))*100
            dati_before_MEMO.append(accuracy)

        elif split_name[1] == "after":
            if len(split_name) == 3:
                data = eval(riga['Result_for_image'])
                tot_correct = 0
                for elem in data:
                    tot_correct += elem[0]
                accuracy = (tot_correct/len(data))*100
                dati_after_MEMO_PLUS.append(accuracy)
            else:
                data = eval(riga['Result_for_image'])
                tot_correct = 0
                for elem in data:
                    tot_correct += elem[0]
                accuracy = (tot_correct/len(data))*100
                dati_after_MEMO.append(accuracy)



# Creazione del plot
plt.figure(figsize=(10, 6))

# Assumendo che i dati siano ordinati per classe o in ordine temporale
plt.plot(dati_before_MEMO, label='Before MEMO', marker='o')
plt.plot(dati_after_MEMO, label='After MEMO', marker='o')

# Aggiungere etichette e titolo
plt.xlabel('Class')
plt.ylabel('Accuracy')
plt.title('Accuracy Before and After MEMO')
plt.legend()

# Salva il grafico in un file
output_path = '/home/sagemaker-user/DeepLearning_project/analize_script/try.jpg'
plt.savefig(output_path)

# Mostrare il grafico
plt.show()

print(f"Il grafico è stato salvato in {output_path}")
