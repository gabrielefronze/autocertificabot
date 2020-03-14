#! /usr/bin/env python3

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from fpdf import FPDF

class birth:
  def __init__(self, date, city):
    self.date = date
    self.city = city

  def printBirth(self):
    return "Nato a {} il {}".format(self.city, self.date)

doc_kinds = {"id" : 1, "passport" : 2, "drivinglic" : 3}

class document:
  def __init__(self, kind , number):
    self.kind = kind
    self.number = number

  def printDocument(self):
    return "Identificato a mezzo {}, numero {}".format(self.kind, self.number)

class address:
  def __init__(self, city, road, number):
    self.city = city
    self.road = road
    self.number = number

  def printAddress(self):
    return "Residente a {}, {} {}".format(self.city, self.road, self.number)

class person:
  def __init__(self, first_name, family_name, birth, address, document, phone):
    self.first_name = first_name
    self.family_name = family_name
    self.birth = birth
    self.address = address
    self.document = document
    self.phone = phone

  def printPerson(self):
    return ("Il sottoscritto {} {}.\n{}.\n{}.\n{}.\nUtenza telefonica {}.\nconsapevole delle conseguenze penali previste in caso di dichiarazioni mendaci a pubblico ufficiale (art 495 c.p.)".format(self.family_name.capitalize(),
                                                                                                                                                                                          self.first_name,
                                                                                                                                                                                          self.address.printAddress(),
                                                                                                                                                                                          self.birth.printBirth(),
                                                                                                                                                                                          self.document.printDocument(),
                                                                                                                                                                                          self.phone))


def printNotice():
  return "DICHIARA SOTTO LA PROPRIA RESPONSABILITÀ\nDi essere a conoscenza delle misure di contenimento del contagio di cui all’art. 1, comma 1, del Decreto del Presidente del Consiglio dei Ministri del 9 marzo 2020 concernenti lo spostamento delle persone fisiche all’interno di tutto il territorio nazionale, nonché delle sanzioni previste dall’art. 4, comma 1, del Decreto del Presidente del Consiglio dei Ministri dell’ 8 marzo 2020 in caso di inottemperanza (art. 650 C.P. salvo che il fatto non costituisca più grave reato)\nChe lo spostamento è determinato da "

reasons = ["comprovate esigenze lavorative.","situazioni di necessità.","motivi di salute.","rientro presso il proprio domicilio, abitazione o residenza."]

def printReason(index):
  return reasons[index]


def printMotivation(motivation):
  return "\n\nA questo riguardo, dichiara che:\n"+motivation

def printFooter():
  return "\n\n\nData, ora e luogo del controllo\n\n\nFirma del dichiarante\n\n\nL’Operatore di Polizia\n\n\n"

def printAll(person, reason = 0, motivation = "Devo cambiare l'acqua ai delfini dell'acquario di Genova."):
    return testPerson.printPerson()+"\n\n"+printNotice()+printReason(reason)+printMotivation(motivation)+printFooter()
    
def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    testBirth = birth("08/10/1991", "Savigliano")
    testName = ["Gabriele", "Fronzé"]
    testDocument = document("Carta d'identità", "AO000000")
    testAddress = address("Cuneo", "Via Roma", "17")

    testPerson = person(testName[1], testName[0], testBirth, testAddress, testDocument, "0000000000")

    print(printAll(testPerson))

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, printAll(testPerson), ln=1, align="C")
    pdf.output("simple_demo.pdf")
