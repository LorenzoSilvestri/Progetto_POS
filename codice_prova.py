import tkinter as tk
from tkinter import messagebox
import mysql.connector
import jinja2
import pdfkit

# Funzione per connettersi al database MySQL
def connect_to_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",       # Sostituisci con il tuo nome utente MySQL
        password="Lorenzo", # Sostituisci con la tua password MySQL
        database="pos_management"
    )
    return conn

# Funzione per generare il POS in formato PDF
def genera_pos():
    # Recupera il nome dell'azienda inserito dall'utente
    nome_azienda = entry_azienda.get()

    # Connessione al database
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)

    try:
        # Query per recuperare i dati dell'azienda e del cantiere
        cursor.execute("""
            SELECT a.id, a.nome, a.indirizzo, a.p_iva, c.nome_cantiere, c.indirizzo_cantiere, c.data_inizio, c.data_fine
            FROM Aziende AS a
            JOIN Cantieri AS c ON a.id = c.id_azienda
            WHERE a.nome = %s
        """, (nome_azienda,))

        azienda_info = cursor.fetchone()  # Recupera un solo record, il primo che corrisponde

        if azienda_info:
            print("Azienda trovata:", azienda_info)  # Debug: stampa i dettagli dell'azienda

            # Recupera i rischi e misure di sicurezza
            cursor.execute("""
                SELECT r.nome_rischio, m.descrizione
                FROM Rischi AS r
                JOIN Misure_di_sicurezza AS m ON r.id = m.id_rischio
                WHERE r.id_cantiere = %s
            """, (azienda_info['id'],))

            rischi = cursor.fetchall()
            print("Rischi e misure di sicurezza:", rischi)  # Debug: stampa i rischi e le misure di sicurezza

            # Impostazione di Jinja2 per il rendering del template
            env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(searchpath="./")
            )
            template = env.get_template("pos_template.html")

            # Creazione del contenuto HTML con i dati del database
            html_content = template.render(
                azienda=azienda_info,
                rischi=rischi
            )

            # Salvataggio del file HTML
            with open("POS_generato.html", "w") as f:
                f.write(html_content)

            # Configurazione di pdfkit con il percorso dell'eseguibile wkhtmltopdf
            config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")  # Sostituisci con il percorso corretto

            # Generazione del PDF da HTML con pdfkit
            pdf_output_path = f"{nome_azienda}_POS.pdf"
            pdfkit.from_file("POS_generato.html", pdf_output_path, configuration=config)

            # Mostra un messaggio di successo
            messagebox.showinfo("POS Generato", f"Il POS è stato generato con successo!\nFile salvato come: {pdf_output_path}")

        else:
            # Se l'azienda non viene trovata nel database
            messagebox.showerror("Errore", "Azienda non trovata nel database!")

    except mysql.connector.Error as err:
        # Gestione dell'errore in caso di problemi con il database
        messagebox.showerror("Errore Database", f"Si è verificato un errore con il database: {err}")

    finally:
        # Assicurati di chiudere la connessione al database
        cursor.close()
        conn.close()

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x150")  # Larghezza x Altezza
root.resizable(False, False)  # Impedisce di ridimensionare la finestra

root.title("Generatore POS")

# Etichetta e campo di input per il nome dell'azienda
label_azienda = tk.Label(root, text="Inserisci il nome dell'azienda:", font=("Arial", 14), fg="blue", bg="lightgrey")
label_azienda.pack(padx=20, pady=10)

entry_azienda = tk.Entry(root)
entry_azienda.pack(padx=20, pady=10)

# Bottone per generare il POS
btn_genera_pos = tk.Button(root, text="Genera POS", command=genera_pos)
btn_genera_pos.pack(padx=20, pady=20)

# Avvio dell'interfaccia grafica
root.mainloop()



