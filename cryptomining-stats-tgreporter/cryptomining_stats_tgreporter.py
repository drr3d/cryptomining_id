from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
import sched, time
import telegram_send
import json

s = sched.scheduler(time.time, time.sleep)
session = HTMLSession()

def miningSoftStatScraper(host_url):
    """
        Fungsi yang digunakan untuk scrapping halaman web yang disediakan
        oleh mining software.
    """
    table=None
    try:
        print("getting session data from host:{}".format(host_url))
        r = session.get(host_url)

        # need this because HTML created by GMiner API is from JavaScript generated data 
        r.html.render()

        # parse rendered session into bs4
        soup = BeautifulSoup(r.html.raw_html, 'html.parser')

        # get table id of GMiner API
        table = soup.find('table', attrs={'id':'device_stat'})
    except:
        print("Warn!! Could not reach Mining Software Web Service on:{}".format(host_url))

    return table

def sendMiningSoftStatsData(sc, host_url, delay_time):
    """
        Fungsi yang digunakan untuk mengirim hasil scrapping web api data
        ke telegram bot.
    """
    print("Doing stuff...")
    
    table = miningSoftStatScraper(host_url)
    if table is not None:
        try:
            # move html data to pandas
            df = pd.read_html(str(table))[0] 

            # convert df to markdown then send it into telegram bot
            telegram_send.send(messages=[df.to_markdown()], parse_mode="markdown")
            print("sended data:{}".format(df.to_markdown()))
        except Exception as e:
            # send df to markdown into telegram bot
            err_messages="Please check your Mining Rig!!! ~ {}".format(e)
            telegram_send.send(messages=[err_messages], parse_mode="text")
            print(err_messages)
    else:
        telegram_send.send(messages=["Warn!! Could not reach Mining Software Web Service on:{}".format(host_url)], parse_mode="text")
    # do your stuff
    s.enter(delay_time, 1, sendMiningSoftStatsData, (sc, host_url, delay_time,))


def main(host_addr, host_port, delay_time=860):
    if host_addr != None and len(host_addr)!=0:
        if type(host_addr)==list:
            print("Starting minersStats Telegram Bot app...")
            print("Using mining soft API host:{}".format(host_addr))
            print("Using mining soft API port:{}".format(host_port))
            print("Scheduler will run every:{} second".format(delay_time))

            for ix,addr in enumerate(host_addr):
                host_url="http://{}:{}".format(addr, host_port[ix])

                # by default host_addr and host_port setting in settings.json should be list type
                #   because it will be used to monitor multiple host at a time.
                # process every ~delay_time second
                print(host_url)
                s.enter(delay_time, 1, sendMiningSoftStatsData, (s, host_url, delay_time,))
            s.run()
        else:
            print("WARNING!! host_addr type is: {} ! list type required...".format(host_addr))
            print("App will terminate...")
    else:
        print("WARNING!! host_addr is: {}".format(host_addr))
        print("App will terminate...")

if __name__== "__main__":
    # load settings file
    # default settings.json will be located at the same directory as this file located.
    with open('settings.json') as svc_cfg:
        _cfg = json.load(svc_cfg)

    main(_cfg['miningsoft_cfg']['host'], _cfg['miningsoft_cfg']['port'], delay_time=_cfg['delay_time'])
