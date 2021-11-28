# Antes de utilizá-lo, será necessário instalar a biblioteca python-telegram-bot:
# pip install python-telegram-bot

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
  update.message.reply_text('Use os comandos acima para receber as informações mais recentes da covid no país.')

def vachoje(update: Update, context: CallbackContext) -> None:
  update.message.reply_text("1ª dose: 43.242\n2ª e única: 230.905 (sendo 22.274 únicas)\n3ª dose: 110.275\nTotal de doses aplicadas hoje: 384.422\nÚltima atualização: 27/11/21 às 17h54")

def vactotal(update: Update, context: CallbackContext) -> None:
  update.message.reply_text("1ª dose: 158.726.663 (74.41% da população)\n2ª e única: 132.626.771 (62.17% da população)\n3ª dose: 15.772.870 (7.39% da população)\nTotal de doses aplicadas: 307.126.304\nÚltima atualização: 27/11/21 às 17h54")

def obithoje(update: Update, context: CallbackContext) -> None:
  update.message.reply_text("Número de óbitos registrados hoje: 1\nÚltima atualização: 27/11/21 às 17h54")

def obittotal(update: Update, context: CallbackContext) -> None:
  update.message.reply_text("Total de óbitos: 614.227\nÚltima atualização: 27/11/21 às 17h54")

def main():
  #Iniciando bot
  updater = Updater("token")
  dispatcher = updater.dispatcher

  dispatcher.add_handler(CommandHandler("start", start))
  dispatcher.add_handler(CommandHandler("vachoje", vachoje))
  dispatcher.add_handler(CommandHandler("obithoje", obithoje))
  dispatcher.add_handler(CommandHandler("vactotal", vactotal))
  dispatcher.add_handler(CommandHandler("obittotal", obittotal))

  updater.start_polling()

  updater.idle()

if __name__ == '__main__':
  main()