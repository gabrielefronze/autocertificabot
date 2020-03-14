# -*- coding: utf8 -*-

import telepot
import mdutils.mdutils
import markdown2pdf3

reasons = ["comprovate esigenze lavorative.","situazioni di necessità.","motivi di salute.","rientro presso il proprio domicilio, abitazione o residenza."]

class person:
  def __init__(self, name="", birth="", address="", document="", phone=""):
    self.name = name
    self.birth = birth
    self.address = address
    self.document = document
    self.phone = phone
    self.reason = -1
    self.motivation = ""

  def printPerson(self, mdfile):
    mdfile.new_line("")
    mdfile.new_line("")
    mdfile.new_header(level=3, title="**AUTODICHIARAZIONE DI SPOSTAMENTO**")
    mdfile.new_paragraph("Il sottoscritto **{}**, residente in **".format(self.name.capitalize())+self.address+"**, nato a **"+self.birth+"**, identificabile tramite **"+self.document+"** e con utenza telefonica **{}**.".format(str(self.phone)))
    mdfile.new_line("")
    mdfile.new_line("Consapevole delle conseguenze penali previste in caso di dichiarazioni mendaci a pubblico ufficiale **(art 495 c.p.)**")

  def showPerson(self):
    return "name: {}\nbirth: {}\naddress: {}\ndocument: {}\nphone: {}\nreason: {}\nmotivation: {}".format(self.name, self.birth, self.address, self.document, self.phone, reasons[self.reason], self.motivation)


def printNotice(mdfile):
  mdfile.new_line("")
  mdfile.new_line("")
  mdfile.new_header(level=4, title="**DICHIARA SOTTO LA PROPRIA RESPONSABILITÀ**")
  mdfile.new_paragraph("* Di essere a conoscenza delle misure di contenimento del contagio di cui all’art. 1, comma 1, del Decreto del Presidente del Consiglio dei Ministri del 9 marzo 2020 concernenti lo spostamento delle persone fisiche all’interno di tutto il territorio nazionale, nonché delle sanzioni previste dall’art. 4, comma 1, del Decreto del Presidente del Consiglio dei Ministri dell’ 8 marzo 2020 in caso di inottemperanza (art. 650 C.P. salvo che il fatto non costituisca più grave reato")

def printReason(index, mdfile):
  mdfile.new_line("* Che lo spostamento è determinato da: **{}**".format(reasons[index]))


def printMotivation(motivation, mdfile):
  mdfile.new_line("")
  mdfile.new_line("")
  mdfile.new_line("A questo riguardo, dichiara che:")
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