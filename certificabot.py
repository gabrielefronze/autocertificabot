#! /usr/bin/env python3
# -*- coding: utf8 -*-

from utils import *
import os
    
TOKEN = 

bot = telepot.Bot(TOKEN)

counter = 0

def main():
    bot.message_loop(on_chat_message)

    print('Listening ...')

    import time
    while 1:
        time.sleep(10)

data_cache = dict()
state_cache = dict()

def on_chat_message(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  telegram_name = msg["from"]["first_name"]

  if telegram_name not in state_cache or state_cache[telegram_name] == "certificabot.start" or state_cache[telegram_name] == None:
    bot.sendMessage(chat_id, "Benvenuto!\nI tuoi dati non verranno salvati e saranno cancellati appena riceverai l'autodichiarazione.\nDevo farti qualche domanda:\n")
    bot.sendMessage(chat_id, "Come ti chiami (Nome e Cognome)?")
    state_cache[telegram_name] = "certificabot.name"
    data_cache[telegram_name] = person()

  elif state_cache[telegram_name] == "certificabot.name":
    data_cache[telegram_name].name = msg['text']
    bot.sendMessage(chat_id, "Dove e quando sei nato (Data, Luogo e sigla della Provincia)?")
    state_cache[telegram_name] = "certificabot.birth"

  elif state_cache[telegram_name] == "certificabot.birth":
    data_cache[telegram_name].birth = msg['text']
    bot.sendMessage(chat_id, "Dove risiedi (città, sigla della Provincia e via)?")
    state_cache[telegram_name] = "certificabot.address"

  elif state_cache[telegram_name] == "certificabot.address":
    data_cache[telegram_name].address = msg['text']
    bot.sendMessage(chat_id, "Qual è il tuo domicilio (città, sigla della Provincia e via)?")
    state_cache[telegram_name] = "certificabot.address2"

  elif state_cache[telegram_name] == "certificabot.address2":
    data_cache[telegram_name].address2 = msg['text']
    bot.sendMessage(chat_id, "Qual è il tuo numero di telefono?")
    state_cache[telegram_name] = "certificabot.phone"

  elif state_cache[telegram_name] == "certificabot.phone":
    data_cache[telegram_name].phone = msg['text']
    bot.sendMessage(chat_id, "Qual è il numero della tua carta d'identita?")
    state_cache[telegram_name] = "certificabot.document"

  elif state_cache[telegram_name] == "certificabot.document":
    data_cache[telegram_name].document = "Carta d'Indentità n."+str(msg['text'])
    bot.sendMessage(chat_id, "Da chi è stato rilasciato?")
    state_cache[telegram_name] = "certificabot.docuauth"

  elif state_cache[telegram_name] == "certificabot.docuauth":
    data_cache[telegram_name].documentAuth = str(msg['text'])
    bot.sendMessage(chat_id, "Da che regione parti?")
    state_cache[telegram_name] = "certificabot.regionstart"

  elif state_cache[telegram_name] == "certificabot.regionstart":
    data_cache[telegram_name].startingRegion = str(msg['text'])
    bot.sendMessage(chat_id, "Da che indirizzo parti?")
    state_cache[telegram_name] = "certificabot.addressstart"

  elif state_cache[telegram_name] == "certificabot.addressstart":
    data_cache[telegram_name].startingAddress = str(msg['text'])
    bot.sendMessage(chat_id, "In che regione vai?")
    state_cache[telegram_name] = "certificabot.regionstop"

  elif state_cache[telegram_name] == "certificabot.regionstop":
    data_cache[telegram_name].destinationRegion = str(msg['text'])
    bot.sendMessage(chat_id, "A che indirizzo arrivi?")
    state_cache[telegram_name] = "certificabot.addressstop"

  elif state_cache[telegram_name] == "certificabot.addressstop":
    data_cache[telegram_name].destinationAddress = str(msg['text'])
    bot.sendMessage(chat_id, "Per quale motivo ti stai spostando?")
    state_cache[telegram_name] = "certificabot.motivation"

  elif state_cache[telegram_name] == "certificabot.motivation":
    data_cache[telegram_name].motivation = msg['text']
    bot.sendMessage(chat_id, "Scrivi \"1\" se per comprovate esigenze lavorative;\nScrivi \"2\" assoluta urgenza (\"per trasferimenti in comune diverso\", come previsto dall’art. 1, comma 1, lettera b) del Decreto del Presidente del Consiglio dei Ministri 22 marzo 2020);\nScrivi \"3\" situazione di necessità (per spostamenti all’interno dello stesso comune o che rivestono carattere di quotidianità o che, comunque, siano effettuati abitualmente in ragione della brevità delle distanze da percorrere);\nScrivi \"4\" se per motivi di salute.")
    state_cache[telegram_name] = "certificabot.reason"

  elif state_cache[telegram_name] == "certificabot.reason":
    index =  int(msg['text'])-1
    # if index >= 0 and index < len(reasons):
    #   bot.sendMessage(chat_id, "Opzione sbagliata!\nScrivi:\n1: se per comprovate esigenze lavorative;\n2: se per situazioni di necessità;\n3: motivi di salute;\n4: se per rientro presso il proprio domicilio, abitazione o residenza")
    #   state_cache[telegram_name] = "certificabot.motivation"
    #   return
    print(index)
    data_cache[telegram_name].reason = index
    bot.sendMessage(chat_id, "Dammi un attimo...")
    global counter
    counter += 1
    bot.sendMessage(chat_id, "Ecco i dati che hai inserito:\n{}".format(data_cache[telegram_name].showPerson()))

    filename = "Autocertificazione_{}".format(data_cache[telegram_name].name)
    mdFile = mdutils.MdUtils(file_name=filename)
    data_cache[telegram_name].printPerson(mdFile)
    printNotice(mdFile, data_cache[telegram_name])
    printReason(data_cache[telegram_name].reason,mdFile)
    printMotivation(data_cache[telegram_name].motivation, mdFile)
    printFooter(mdFile)
    mdFile.create_md_file()

    markdown2pdf3.convert_markdown_to_pdf("./{}.md".format(filename))

    bot.sendDocument(chat_id, open("./{}.pdf".format(filename),"rb") ,caption="Ecco qui la tua autocertificazione! Sii prudente!")

    os.remove("./{}.md".format(filename))
    os.remove("./{}.pdf".format(filename))

    state_cache[telegram_name] = None
    data_cache[telegram_name] = None

    state_cache[telegram_name] = "certificabot.start"


if __name__ == '__main__':
  main()
