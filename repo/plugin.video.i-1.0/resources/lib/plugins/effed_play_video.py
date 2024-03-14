import json
import re
import xbmc
import xbmcgui
import xbmcaddon
from requests.sessions import Session
from ..plugin import Plugin


addon_id = xbmcaddon.Addon().getAddonInfo('id')
default_icon = xbmcaddon.Addon(addon_id).getAddonInfo('icon')
base_url = 'https://www.effedupmovies.com/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
headers = {
    'User-Agent': user_agent,
    'Referer': base_url
}
session = Session()
session.headers = headers


class default_play_video(Plugin):
    name = "effed video playback"
    priority = 1000
    
    def play_video(self, item):
        if 'effedupmovies.com' in str(item):
            item = json.loads(item)
            link = item.get("link", "")
            if link == "":
                return False
            page = session.get(link).text
            link = re.findall('source src="(.+?)" ', page)
            if link:
                link = link[0].strip()
            else:
                return False
            title = item["title"]
            thumbnail = item.get("thumbnail", default_icon)
            summary = item.get("summary", "")
            liz = xbmcgui.ListItem(title)
            if item.get("infolabels"):
                liz.setInfo("video", item["infolabels"])
            else:
                liz.setInfo("video", {"title": title, "plot": summary})
            liz.setArt({"thumb": thumbnail, "icon": thumbnail, "poster": thumbnail})
            xbmc.Player().play(link, liz)
            return True