#! /usr/bin/env python3
# -*- coding: utf8 -*-

from utils import *
import os

def main():
    testPerson =  person("Pippo", "4 dicembre 1976", "via vattialapesca, Cuneo", "Carta d'Indentità n.AO000000", "3390000000")
    testPerson.reason = 2
    testPerson.motivation = "Portare a spasso il cane"

    filename = "Autocertificazione_{}".format(testPerson.name)
    mdFile = mdutils.MdUtils(file_name=filename)
    testPerson.printPerson(mdFile)
    printNotice(mdFile)
    printReason(testPerson.reason,mdFile)
    printMotivation(testPerson.motivation, mdFile)
    printFooter(mdFile)
    mdFile.create_md_file()

    markdown2pdf3.convert_markdown_to_pdf("./{}.md".format(filename))

if __name__ == '__main__':
  main()