import html

import bs4
import requests
from Mitsuri import dispatcher
from Mitsuri.modules.disable import DisableAbleCommandHandler
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode,
                      Update)
from telegram.ext import CallbackContext

info_btn = "More Information"
kayo_btn = "Est 🏴‍☠️"
air_btn = "Air 🏴‍☠️"
animespot_btn = "Classic ☠️"
animetm_btn = "Hsa ☠️"
prequel_btn = "⬅️ Prequel"
sequel_btn = "Sequel ➡️"
close_btn = "Close ❌"


def site_search(update: Update, context: CallbackContext, site: str):
    message = update.effective_message
    args = message.text.strip().split(" ", 1)
    more_results = True

    try:
        search_query = args[1]
    except IndexError:
        message.reply_text("Give something to search")
        return

    if site == "est":
        search_url = f"https://animehindisub.com/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"})

        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>EST Anime</code>: \n"
        for entry in search_result:

            if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>EST Anime</code>"
                more_results = False
                break

            post_link = entry.a['href']
            post_name = html.escape(entry.text.strip())
            result += f"• <a href='{post_link}'>{post_name}</a>\n"

    elif site == "air":
        search_url = f"https://subbedacademy.blogspot.com/search?q={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"}) 
        
        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>Anime Air</code>: \n"
        for entry in search_result:
                 
           if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>Anime Air</code>"
                more_results = False
                break
                
        post_link = entry.a['href'] if entry.a else None
        if post_link:
           post_name = html.escape(entry.text.strip())
           result += f"• <a href='{post_link}'>{post_name}</a>\n"
            
    elif site == "classic":
        search_url = f"https://www.chineseanimehindisub.online/search?q={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"}) 
        
        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>Chinese Anime Hindi Sub</code>: \n"
        for entry in search_result:
                 
           if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>Chinese Anime Hindi Sub</code>"
                more_results = False
                break
                
           post_link = entry.a['href']
           post_name = html.escape(entry.text.strip())
           result += f"• <a href='{post_link}'>{post_name}</a>\n"
           
    elif site == "hsa":
        search_url = f"https://hsaanime.in/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"}) 
        
        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>HSA Anime</code>: \n"
        for entry in search_result:
                 
           if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>HSA Anime</code>"
                more_results = False
                break
                
           post_link = entry.a['href']
           post_name = html.escape(entry.text.strip())
           result += f"• <a href='{post_link}'>{post_name}</a>\n"
           
    buttons = [[InlineKeyboardButton("See all results", url=search_url)]]

    if more_results:
        message.reply_text(
            result,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True)
    else:
        message.reply_text(
            result, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def est(update: Update, context: CallbackContext):
    site_search(update, context, "est")
  
def air(update: Update, context: CallbackContext):
    site_search(update, context, "air")
    
def classic(update: Update, context: CallbackContext):
    site_search(update, context, "classic")
   
def hsa(update: Update, context: CallbackContext):
    site_search(update, context, "hsa")


EST_SEARCH_HANDLER = DisableAbleCommandHandler("est", est, run_async = True)
AIR_SEARCH_HANDLER = DisableAbleCommandHandler("air", air, run_async = True)
CLASSIC_SEARCH_HANDLER = DisableAbleCommandHandler("classic", classic, run_async = True)
HSA_SEARCH_HANDLER = DisableAbleCommandHandler("hsa", hsa, run_async = True)

dispatcher.add_handler(EST_SEARCH_HANDLER)
dispatcher.add_handler(AIR_SEARCH_HANDLER)
dispatcher.add_handler(CLASSIC_SEARCH_HANDLER)
dispatcher.add_handler(HSA_SEARCH_HANDLER)

__handlers__ = [ EST_SEARCH_HANDLER, AIR_SEARCH_HANDLER,
     CLASSIC_SEARCH_HANDLER,  HSA_SEARCH_HANDLER]
