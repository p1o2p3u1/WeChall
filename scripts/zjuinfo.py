import BeautifulSoup
import requests
import pymongo
connection = pymongo.Connection('localhost', 27017)
db = connection.ZJU
StudentInfo = db.StudentInfo
postData1 = 'Action=applyfilter&StateAction=samePageState&Done=ReloadDashboard&Page=%E7%A0%94%E7%A9%B6%E7%94%9F%E6%9F%A5%E8%AF%A2%E6%9C%8D%E5%8A%A1&PortalPath=%2Fshared%2F%E4%BB%AA%E8%A1%A8%E7%9B%98%2F_portal%2F+%E9%9D%A2%E5%90%91%E5%B8%88%E7%94%9F%E6%9F%A5%E8%AF%A2&P0=%3Csawx%3Aexpr+xmlns%3Asawx%3D%22com.siebel.analytics.web%2Fexpression%2Fv1%22+xsi%3Atype%3D%22sawx%3Alist%22+op%3D%22in%22+xmlns%3Axsi%3D%22http%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema-instance%22%3E%3Csawx%3Aexpr+xsi%3Atype%3D%22sawx%3AsqlExpression%22%3EZXS_ALL.%22%E5%AD%A6%E5%8F%B7%22%3C%2Fsawx%3Aexpr%3E%3Csawx%3Aexpr+xsi%3Atype%3D%22sawx%3AuntypedLiteral%22%3E'
postData2 = '%3C%2Fsawx%3Aexpr%3E%3C%2Fsawx%3Aexpr%3E&P1=page&P2=&P3=&P4=&P5=&P6=&P7=&P8=&P9=&P10=&P11=&P12=&P13=&P14=&P15=&P16=&P17=&P18=&P19=&ViewID=&reloadTargets=all&Caller=Dashboard'

image_url = 'http://zudc.zju.edu.cn/tsc/dc/tsc/controller/photo.do?pid=%s'
login_url = 'http://zudc.zju.edu.cn/saw.dll?Dashboard'

def _login():
    login_data = 'NQUser=21301001&NQPassword=zju_wiscom&saveLangPref=true&icharset=utf-8'
    r = requests.post(login_url, login_data)
    n_quire_id = r.cookies['nQuireID']
    saw_username = r.cookies['sawU']
    saw_password = ''
    cookie = {
        'nQuireID': n_quire_id,
        'sawU': saw_username,
        'sawP': saw_password
    }
    return cookie


def _post_data_graduate(stu_number):
    cookie = _login()
    table = None
    loop_time = 0
    while table is None and loop_time < 10:
        loop_time += 1
        r = requests.post(login_url, postData1 + stu_number + postData2, cookies=cookie)
        html = r.content
        soup = BeautifulSoup.BeautifulSoup(html)
        table = soup.find('div', id='idResultsTableParent')
        if table is None:
            if loop_time == 10:
                print "no such people: %s" % stu_number
                return None
            else:
                continue
        else:
            info = table.findAll('td')
            sid = _trim_and_replace(info[0].text)
            name = _trim_and_replace(info[1].text)
            sex = _trim_and_replace(info[2].text)
            birthday = _trim_and_replace(info[3].text)
            address = _trim_and_replace(info[4].text)
            department = _trim_and_replace(info[5].text)
            profession = _trim_and_replace(info[6].text)
            enrol = _trim_and_replace(info[7].text)
            cultivation = _trim_and_replace(info[8].text)
            tutorid = _trim_and_replace(info[9].text)
            image = requests.get(image_url % stu_number)
            if len(image.content) == 1799:
                avatar = ''
                print 'no pic you say a jb'
            else:
                avatar = image.content.encode('base64')

            record = {
                "sid": sid,
                "name": name,
                "sex": sex,
                "birthday": birthday,
                "address": address,
                "department": department,
                "profession": profession,
                "enrol": enrol,
                "cultivation": cultivation,
                "tutorid": tutorid,
                'Avatar': avatar
            }
            StudentInfo.insert(record)
            print stu_number
            return 'OK'


def _trim_and_replace(text):
    if text is None:
        return ''
    else:
        return text.strip().replace('&nbsp;', '')

'''
def _get_stu_nos():
    init_list = []
    download_list = []
    for degree in range(1, 3):
        for grade in [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
            for dept in range(1, 50):
                for id in xrange(1, 999):
                    stu_number = '%d%02d%02d%03d' % (degree, grade, dept, id)
                    init_list.append(stu_number)

    sids = list(StudentInfo.find({}, {'sid': 1}))
    for sid in sids:
        download_list.append(sid['sid'])

    student_nos = set(init_list) - set(download_list)
    return student_nos
'''


if __name__ == '__main__':
    # 2 13 21 235
    # 1=doctor, 2=master, 3=bachelor
    # 13 = grade
    # 21 = computer science
    # 235 = student id
    sids = list(StudentInfo.find({}, {'sid': 1}))
    download_list = []
    for sid in sids:
        download_list.append(sid['sid'])
    print download_list

    for degree in range(1, 3):
        for grade in [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
            for dept in range(1, 50):
                fail = 0
                for id in xrange(1, 999):
                    stu_number = '%d%02d%02d%03d' % (degree, grade, dept, id)
                    if stu_number not in download_list:
                        result = _post_data_graduate(stu_number)
                        if result is None:
                            fail += 1
                            if fail > 10:
                                break
                        else:
                            fail = 0
                    else:
                        print "Downloaded."
