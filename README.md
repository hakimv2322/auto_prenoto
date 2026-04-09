# auto_prenoto

**Step 1: Installare Python e pip (per installare i package di python)**  
 - Scaricare Python: https://www.python.org/downloads/  
 - Adesso puoi entrare in un environment python in Terminal (Mac/Linux) o CommandPrompt (Windows) con il comando:
 
    ```python3```
 - Assicurati di avere pip installato: https://pip.pypa.io/en/stable/installation/

**Step 2: Usare pip per installare Selenium, Schedule, e Pytz.**  
Tutti i seguenti comandi verranno fatti in Terminal (ma non in un environment python).
 - [Selenium](https://selenium-python.readthedocs.io/installation.html), per interagire con le webpage:  

   ```pip install selenium```
 - [Schedule](https://schedule.readthedocs.io/en/stable/installation.html), per schedulare azioni:

   ```pip install schedule```
 - [Pytz](https://pypi.org/project/pytz/), per sistemare i timezone:  

   ```pip install pytz```

**Step 3: Creare una "App Password" per la tua e-mail.**  
Questo step è facoltativo, se vuoi le notifiche inviate alla tua e-mail. Le e-mail sono inviate solo nel caso di fallimento, non durante comportamento nominale. Io consiglierei di attivare le notifiche e-mail perché altrimenti sarà difficile accorgersi di un fallimento.
 - Segui le istruzioni qui: https://support.google.com/mail/answer/185833?hl=en
 - Deve essere G-mail. Se crei una nuova G-mail, crearne una con un'età di almeno 18 anni.
 - Questa "app password" servirebbe per fare lo script accedere alla tua e-mail per mandare la mail. Sarà una password valida solo per un dispositivo.
 - Puoi testare questa funzionalità settando "test_email_sending" come "True", che manderà una mail ogni 5 secondi.

**Step 4: Scaricare lo script auto_prenoto.py e settare gli input.**  
Scaricare sul tuo dispositivo, per esempio in "Documents". Scegli tutti gli input che vuoi, inserendo qui la "app password" di Step 3 (no spazi).

**Step 5: Run.**
 - In Terminal, navigare alla cartella in cui hai messo auto_prenoto.py. (Puoi navigare con il comando "cd".) Avviare lo script con:

   ```python3 auto_prenoto.py```
 - Questa finestra di Terminal, purtroppo, esisterà sempre. A meno che non chiuda la finestra, starà sempre runnando. Minimizare e ignorarla.
 - Assicurati che il tuo computer **non vada mai in sleep**. Per il mio Mac, ho dovuto seguire le istruzioni [qui](https://superuser.com/questions/1018140/keep-macbook-running-with-lid-closed-for-specified-duration), cioè:

   ```sudo pmset -b sleep 0; sudo pmset -b disablesleep 1```
   
   (Attenzione quando non è attacato all'allimentatore.) Se il computer va in sleep, lo script sarà pausato e non farà niente. Però si riprenderà quando il computer si risveglia.
 - Se riavvi il tuo computer, devi rilanciare lo script.






