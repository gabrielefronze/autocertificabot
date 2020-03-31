# -*- coding: utf8 -*-

import telepot
import mdutils.mdutils
import markdown2pdf3

reasons = ["comprovate esigenze lavorative.","assoluta urgenza (\"per trasferimenti in comune diverso\", come previsto dall’art. 1, comma 1, lettera b) del Decreto del Presidente del Consiglio dei Ministri 22 marzo 2020).","situazione di necessità (per spostamenti all’interno dello stesso comune o che rivestono carattere di quotidianità o che, comunque, siano effettuati abitualmente in ragione della brevità delle distanze da percorrere).","motivi di salute."]

class person:
  def __init__(self, name="", birth="", address="", document="", phone="", documentAuth=""):
    self.name = name
    self.birth = birth
    self.address = address
    self.address2 = address
    self.document = document
    self.documentAuth = documentAuth
    self.phone = phone
    self.reason = -1
    self.motivation = ""
    self.startingRegion = ""
    self.startingAddress = ""
    self.destinationRegion = ""
    self.destinationAddress = ""

  def printPerson(self, mdfile):
    mdfile.new_line("")
    mdfile.new_line("")
    mdfile.new_header(level=3, title="**AUTODICHIARAZIONE AI SENSI DEGLI ARTT. 46 E 47 D.P.R. N. 445/2000**")
    mdfile.new_line("Il sottoscritto **{}**,".format(self.name.capitalize())+"nato il **"+self.birth+"**,"+"residente in **"+self.address+"**,"+"domiciliato in **"+self.address2+"**,"+"identificato a mezzo **"+self.document+"**,"+"rilasciato da **"+self.documentAuth+"**,"+"e con utenza telefonica **{}**.".format(str(self.phone)))
    mdfile.new_line("Consapevole delle conseguenze penali previste in caso di dichiarazioni mendaci a pubblico ufficiale **(art 495 c.p.)**")

  def showPerson(self):
    return "name: {}\nbirth: {}\naddress: {}\ndocument: {}\nphone: {}\nreason: {}\nmotivation: {}".format(self.name, self.birth, self.address, self.document, self.phone, reasons[self.reason], self.motivation)


def printNotice(mdfile, person):
  mdfile.new_line("")
  mdfile.new_line("")
  mdfile.new_header(level=4, title="**DICHIARA SOTTO LA PROPRIA RESPONSABILITÀ**")
  mdfile.new_paragraph("* **di non essere sottoposto alla misura della quarantena ovvero di non essere risultato positivo al COVID-19** __(fatti salvi gli spostamenti disposti dalle Autorità sanitarie)__;")
  mdfile.new_paragraph("* che lo spostamento è iniziato da **{}** con destinazione **{}**;".format(person.startingAddress, person.destinationAddress))
  mdfile.new_paragraph("* **di essere a conoscenza delle misure di contenimento del contagio vigenti alla data odierna ed adottate ai sensi degli artt. 1 e 2 del decreto legge 25 marzo 2020, n. 19, concernenti le limitazioni alle possibilità di spostamento delle persone fisiche all’interno di tutto il territorio nazionale**;")
  mdfile.new_paragraph("* **di essere a conoscenza delle ulteriori limitazioni disposte con provvedimenti del Presidente della Regione {} e del Presidente della Regione {} e che lo spostamento rientra in uno dei casi consentiti dai medesimi provvedimenti: {}**;".format(person.startingRegion, person.destinationRegion, person.motivation))
  mdfile.new_paragraph("* **di essere a conoscenza delle sanzioni previste dall’art. 4 del decreto legge 25 marzo 2020, n. 19**;")

def printReason(index, mdfile):
  mdfile.new_line("* Che lo spostamento è determinato da: **{}**".format(reasons[index]))


def printMotivation(motivation, mdfile):
  mdfile.new_line("")
  mdfile.new_line("")
  mdfile.new_header(level=4, title="A questo riguardo, dichiara che:")
  mdfile.new_line("**{}**".format(motivation))

def printFooter(mdfile):
  # mdfile.new_line("<style> table { width:100%; border: none; border-top: none; sborder-left: none; sborder-bottom: none; sborder-right: none; } </style>")
  mdfile.new_line("")
  mdfile.new_line("")
  mdfile.new_line("")
  mdfile.new_header(level=4, title="Data e ora del controllo: _________________________")
  mdfile.new_line("")
  mdfile.new_line("")
  mdfile.new_line("")
  mdfile.new_header(level=4, title="Firma del dichiarante: _________________________")
  mdfile.new_line("")
  mdfile.new_line("")
  mdfile.new_line("")
  mdfile.new_header(level=4, title="L'Operatore di Polizia: _________________________")

def printAll(person, reason = 0, motivation = "Devo cambiare l'acqua ai delfini dell'acquario di Genova."):
    return person.printPerson()+"\n\n"+printNotice()+printReason(reason)+printMotivation(motivation)+printFooter()