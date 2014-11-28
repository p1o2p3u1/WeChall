import requests
import json
import BeautifulSoup
import threading
import logging
import logging.config
import pymongo
import re


acUrl = 'http://www.acfun.tv/a/ac%d'
visitUrl = 'http://www.acfun.tv:80/content_view.aspx?contentId=%d'
tagUrl = 'http://www.acfun.tv:80/member/collect_up_exist.aspx?contentId=%d'
likeUrl = 'http://search.acfun.tv/like?id=ac%d'
acid = 247350
lock = threading.RLock()
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('logger')


class MyThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.thread_name = name

    def __getMongoCollection(self, name):
        conn = pymongo.Connection('192.168.13.170', 27017)
        db = conn.ACFun
        collection = db[name]
        return collection

    def run(self):
        global logger
        global acid
        raw_response = self.__getMongoCollection('RawResponse')
        posts = self.__getMongoCollection('Posts')
        while True:
            lock.acquire()
            acid += 1
            myid = acid
            if myid > 1000000:
                logger.info('done')
                lock.release()
                break
            lock.release()
            url = acUrl % myid
            try:
                r = requests.get(url)
                html = r.content
                if r.status_code != 200:
                    response = {
                        'acid': myid,
                        'url': url,
                        'status_code': r.status_code,
                        'response_headers': dict(r.headers),
                        'content': ''
                    }
                    raw_response.insert(response)
                    continue

                response = {
                    'acid': myid,
                    'url': url,
                    'status_code': r.status_code,
                    'response_headers': dict(r.headers),
                    'content': html
                }
                raw_response.insert(response)

                soup = BeautifulSoup.BeautifulSoup(html)
                result = {}
                result['AcId'] = myid
                title_area = soup.find('div', id='area-title-view')
                result['title'] = title_area.div.h1.text
                title_area_a = title_area.div.p.findAll('a')
                result['category'] = title_area_a[1].text
                result['contributor'] = title_area_a[2].text
                result['datetime'] = title_area.div.p.span.text
                info_view = soup.find('div', id='block-info-view')
                desc = info_view.div.p.text
                result['description'] = desc.replace('&nbsp;', ' ')

                r2 = requests.get(likeUrl % myid)
                content = json.loads(r2.content)
                recommend = content['data']['page']['list']
                result['recommend'] = recommend

                visits = requests.get(visitUrl % myid)
                visits_json = json.loads(visits.content)
                result['hits'] = visits_json[0]
                result['comments'] = visits_json[1]
                result['praise'] = visits_json[3]
                result['favourites'] = visits_json[5]

                tags = requests.get(tagUrl % myid)
                tags_json = json.loads(tags.content)
                result['tags'] = tags_json
                posts.insert(result)
                logger.info("finish id: %d" % myid)

            except Exception, e:
                response = {
                    'acid': myid,
                    'url': url,
                    'status_code': 'Error',
                    'response_headers': '',
                    'content': e.message
                }
                raw_response.insert(response)
                logger.error('fail to pull acid %d' % myid)
                logger.error(e)

def main():
    for i in range(10):
        MyThread(str(i)).start()

if __name__ == '__main__':
    main()
