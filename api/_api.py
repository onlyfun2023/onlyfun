#!/usr/bin/python3
import tornado.ioloop
import tornado.web
import json
from web3.auto import w3
from web3 import Web3
from eth_account.messages import encode_defunct
import binascii
import sqlite3
import base64
import hmac
import queue
import _thread
import time
from beem.steem import Steem
from beem.account import Account
from beembase import operations
from beem.transactionbuilder import TransactionBuilder
from beembase.signedtransactions import Signed_Transaction
import hashlib
import time
from binascii import hexlify
import copy
import random
import requests
from beemgraphenebase.account import PasswordKey
from ast import literal_eval

con = sqlite3.connect('userdatadfaisdhioh%^&%23127ydd.db')
cur = con.cursor()
con_q = sqlite3.connect('userdatadfaisdhioh455dsds%^*&*&62dd.db')
cur_q = con_q.cursor()

q = queue.Queue()
q2 = queue.Queue()
nodes = 'https://api.steemit.com'
#nodes = 'https://api.justyy.com'

class Funtion(object):

    def md5(self, content):
        content = str(content) + "welcome!onlussjdhkjsiuyhjs"
        md5 = hashlib.md5(content.encode(encoding='UTF-8')).hexdigest()
        return md5

    def md5_2(self, content):
        content = str(content)
        md5 = hashlib.md5(content.encode(encoding='UTF-8')).hexdigest()
        return md5

    def verifyamessage(self,addr,hash):
        try:
            msg = "welcome!onlussjdhkjsiuyhjs"
            public_key = hash
            public_key = public_key.replace("0x", "")
            message = encode_defunct(text=msg)
            # addr=w3.eth.account.recover_message(message, signature=signed_message.signature)
            ver_addr = w3.eth.account.recover_message(message, signature=bytes.fromhex(public_key))
            if ver_addr.lower() == addr.lower():
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def Password(self,metadata):
        try:
            db_table = "none"
            if metadata['user'] != "none":
                db_table = metadata['user'][-2:]
            try:
                int(db_table[0])
                db_table = "a" + db_table
            except:
                pass
            db_table2 = "none"
            if metadata['eth_account'] != "none":
                db_table2 = metadata['eth_account'][-2:]
            try:
                int(db_table2[0])
                db_table2 = "a" + db_table2
            except:
                pass
            for i in metadata:
                metadata[i] = str(metadata[i])
            if db_table != "none":
                cur.execute(
                    "REPLACE INTO %s VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        db_table, metadata['user'], metadata['md5'], metadata['user_name'], metadata['email'],
                        metadata['eth_account'], metadata['steem_id'], metadata['invitedId'], metadata['integral'],
                        metadata['token_num'],
                        metadata['lock_token'], metadata['auth_info'], metadata['spread_award_info'],
                        metadata['auction_info'],
                        metadata['buy_article'], metadata['essay_info'], metadata['countdown'], metadata['prepare_info'],
                        metadata['goods'], metadata['status'], metadata['phone'],
                        metadata['avatar'], metadata['activation']))
            if db_table2 != "none":
                cur.execute(
                    "REPLACE INTO %s VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        db_table2, metadata['user'], metadata['md5'], metadata['user_name'], metadata['email'],
                        metadata['eth_account'], metadata['steem_id'], metadata['invitedId'], metadata['integral'],
                        metadata['token_num'],
                        metadata['lock_token'], metadata['auth_info'], metadata['spread_award_info'],
                        metadata['auction_info'],
                        metadata['buy_article'], metadata['essay_info'], metadata['countdown'], metadata['prepare_info'],
                        metadata['goods'], metadata['status'], metadata['phone'],
                        metadata['avatar'], metadata['activation']))
            con.commit()
        except Exception as e:
            print(e)

    def join(self,types,player,name):
        db_table = str(player)[-2:]
        try:
            int(db_table[0])
            db_table = "a" + db_table
        except:
            pass
        if len(player) > 20:
            whois = 'select * from %s where eth_account= "%s"' % (db_table, player)
        else:
            whois = 'select * from %s where user= "%s"' % (db_table, player)
        cur.execute(whois)
        vip = cur.fetchall()
        buy_article = vip[0][13]
        if buy_article == "none":
            if types == "+":
                buy_article = name
        else:
            buy_article = buy_article.split(',')
            if types == "+":
                buy_article.append(name)
            elif types == "-":
                buy_article.remove(name)
            buy_article = ','.join(buy_article)
        if buy_article == "":
            buy_article = "none"
        metadata = {'user': vip[0][0],
                    'md5': vip[0][1],
                    'user_name': vip[0][2],
                    'email': vip[0][3],
                    'eth_account': vip[0][4],
                    'steem_id': vip[0][5],
                    'invitedId': vip[0][6],
                    'integral': vip[0][7],
                    'token_num': vip[0][8],
                    'lock_token': vip[0][9],
                    'auth_info': vip[0][10],
                    'spread_award_info': vip[0][11],
                    'auction_info': vip[0][12],
                    'buy_article': str(buy_article),
                    'essay_info': vip[0][14],
                    'countdown': vip[0][15],
                    'prepare_info': vip[0][16],
                    'goods': vip[0][17],
                    'status': vip[0][18],
                    'phone': vip[0][19],
                    'avatar': vip[0][20],
                    'activation': vip[0][21]}

        run = self.Password(metadata)


    def new(self,player, password, eth_account, invitedId):
        if password == "none":
            md5_data = "none"
        else:
            md5_data = password
        try:
            player = player.lower()
            eth_account = eth_account.lower()
        except:
            pass
        if player == "none":
            steem_id = "q" + funtion.md5(str(eth_account).lower())[0:8]
        else:
            steem_id = "q" + funtion.md5(str(player).lower())[0:8]
        user_name = "none"
        email = "none"
        phone = "none"

        db_table = "none"
        if player != "none":
            db_table = str(player)[-2:]
            try:
                int(db_table[0])
                db_table = "a" + db_table
            except:
                pass

        db_table2 = "none"
        if eth_account != "none":
            db_table2 = str(eth_account)[-2:]
        try:
            int(db_table2[0])
            db_table2 = "a" + db_table2
        except:
            pass

        try:
            if player == "none":
                whois = 'select * from %s where eth_account= "%s"' % (db_table, eth_account)
            else:
                whois = 'select * from %s where user= "%s"' % (db_table, player)
            cur.execute(whois)
            vip = cur.fetchall()
            if vip == []:
                print("new name")
                if db_table != "none":
                    cur.execute(
                        "REPLACE INTO %s VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            db_table, player, md5_data, user_name, email, eth_account, steem_id, invitedId, "none", "0",
                            "0", "none", "none",
                            "none",
                            "none", "none", "none", "none", "none", "none", "none",
                        "none","0"))
                if db_table2 != "none":
                    cur.execute(
                        "REPLACE INTO %s VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            db_table2, player, md5_data, user_name, email, eth_account, steem_id, invitedId, "none",
                            "0", "0", "none", "none",
                            "none",
                            "none", "none", "none", "none", "none", "none", "none",
                        "none","0"))
                con.commit()
            else:
                print("已有用户:",player,eth_account)
        except Exception as e:
            print(e, "--------------------------------------")
            if "no such table" in str(e):
                try:
                    print("no table")
                    if db_table != "none":
                        whois = "CREATE TABLE %s (user TEXT,md5 TEXT,user_name TEXT,email TEXT,eth_account TEXT,steem_id TEXT,invitedId TEXT,integral TEXT,token_num TEXT,lock_token TEXT," \
                                "auth_info TEXT,spread_award_info TEXT,auction_info TEXT,buy_article TEXT,essay_info TEXT,countdown TEXT,prepare_info TEXT," \
                                "goods TEXT,status TEXT,phone TEXT,avatar TEXT,activation TEXT,PRIMARY KEY (user,eth_account))" % db_table
                        cur.execute(whois)
                    if db_table2 != "none":
                        whois = "CREATE TABLE %s (user TEXT,md5 TEXT,user_name TEXT,email TEXT,eth_account TEXT,steem_id TEXT,invitedId TEXT,integral TEXT,token_num TEXT,lock_token TEXT," \
                                "auth_info TEXT,spread_award_info TEXT,auction_info TEXT,buy_article TEXT,essay_info TEXT,countdown TEXT,prepare_info TEXT," \
                                "goods TEXT,status TEXT,phone TEXT,avatar TEXT,activation TEXT,PRIMARY KEY (user,eth_account))" % db_table2
                        cur.execute(whois)
                    con.commit()
                    print("CREATE TABLE", db_table)
                    if db_table != "none":
                        cur.execute(
                            "REPLACE INTO %s VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                                db_table, player, md5_data, user_name, email, eth_account, steem_id, invitedId, "none",
                                "0", "0", "none", "none", "none",
                                "none", "none", "none", "none", "none", "none", "none",
                            "none","0"))
                    if db_table2 != "none":
                        cur.execute(
                            "REPLACE INTO %s VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                                db_table2, player, md5_data, user_name, email, eth_account, steem_id, invitedId, "none",
                                "0", "0", "none", "none", "none",
                                "none", "none", "none", "none", "none", "none", "none",
                            "none","0"))
                    con.commit()
                except Exception as e:
                    print(e)

    def Create_quan(self,post_data):

        #post_data = {"id": "", "token": "", "user_name": "", "steem_id": "", " subscriptions_name": "","introduction": "", "image": "", "price": ""}
        try:
            name = post_data["subscriptions_name"]
            user = post_data["id"]
            user_name = post_data["user_name"]
            steem_id = post_data["steem_id"]
            introduction = post_data["introduction"]
            image = post_data["image"]
            price = post_data["price"]

            time_stamp = int(time.time())
            cur_q.execute("REPLACE INTO quan VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
            name, user, user_name, steem_id, introduction, image, price, time_stamp))
            con_q.commit()

            try:

                steem_name = ("s" + funtion.md5_2(name)[0:10]).lower()
                whois = "CREATE TABLE %s (" \
                        "user TEXT," \
                        "usde_name TEXT," \
                        "steem_id TEXT," \
                        "time_stamp TEXT,PRIMARY KEY (user,usde_name))" % steem_name
                cur_q.execute(whois)
                con_q.commit()
            except Exception as e:
                print(e)

            cur_q.execute(
                "REPLACE INTO %s VALUES('%s','%s','%s','%s')" % (steem_name, user, user_name, steem_id, time_stamp))
            con_q.commit()

        except Exception as e:
            print("error", e)

funtion = Funtion()





class tokens():
    def set(self,player):
        self.player = player
        self.key = player + "OmdsadasMxNDksdas5ZWJhsdfasasdasdasMjc3NWgdsfdsfdsM4OGsdsdasdasRj"

    def generate_token(self, expire=3600):

        ts_str = str(time.time() + expire)
        ts_byte = ts_str.encode("utf-8")
        sha1_tshexstr = hmac.new(self.key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
        token = ts_str + ':' + sha1_tshexstr
        b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
        return b64_token.decode("utf-8")

    def certify_token(self, token):
        r'''
            @Args:
                key: str
                token: str
            @Returns:
                boolean
        '''
        try:
            token_str = base64.urlsafe_b64decode(token).decode('utf-8')
            token_list = token_str.split(':')
            if len(token_list) != 2:
                return False
            ts_str = token_list[0]
            if int(float(ts_str)) < int(time.time()):
                return False
            known_sha1_tsstr = token_list[1]
            sha1 = hmac.new(self.key.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
            calc_sha1_tsstr = sha1.hexdigest()
            if calc_sha1_tsstr != known_sha1_tsstr:
                # token certification failed
                return False
            # token certification success
            return True
        except:
            return False

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with,token")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header("Access-Control-Max-Age", 1000)
        self.set_header("Content-type", "application/json")

    def options(self):
        # 返回方法1
        self.set_status(200)
        self.finish()

class MainHandler(BaseHandler):
    # get请求
    def get(self):
        self.write("Hello world")





class quan(BaseHandler):
    def post(self):
        print("/subscriptions")
        ver = False
        re = True
        try:
            post_data = self.request.body.decode('utf-8')
            print(post_data, type(post_data))
            post_data = json.loads(post_data)
            player = post_data["id"]
            usertoken = post_data["token"]
            v = tokens()
            v.set(player)
            ver = v.certify_token(usertoken)
            if ver == False:
                self.write({'success': 'fail', 'error': 'error token', 'error_code': -1})
        except Exception as e:
            self.write({'success': 'fail', 'error': str(e), 'error_code': 500})

        if ver == True:
            name = post_data["subscriptions_name"]
            try:
                whois = 'select * from quan where name= "%s"' % name
                cur_q.execute(whois)
                vip = cur_q.fetchall()
            except:
                whois = "CREATE TABLE quan (" \
                        "name TEXT," \
                        "user TEXT," \
                        "user_name TEXT," \
                        "steem_id TEXT," \
                        "introduction TEXT," \
                        "image TEXT," \
                        "price TEXT," \
                        "time_stamp TEXT,PRIMARY KEY (name))"
                cur_q.execute(whois)
                con_q.commit()
                vip = []
            if vip == []:
                q2.put(["create_quan",post_data])
                q.put(["quan_join", [player,name]])
                self.write({'success': 'ok'})
            else:
                if vip[0][1] == post_data["id"] :
                    q2.put(["create_quan", post_data])
                    self.write({'success': 'ok'})
                else:
                    self.write({'success': 'fail','error':'already exists','error_code':-1})



class quan_join(BaseHandler):
    def post(self):
        ver = False
        re = True
        try:
            post_data = self.request.body.decode('utf-8')
            print(post_data, type(post_data))
            post_data = json.loads(post_data)
            player = post_data["id"]
            usertoken = post_data["token"]
            v = tokens()
            v.set(player)
            ver = v.certify_token(usertoken)
            if ver == False:
                self.write({'success': 'fail', 'error': 'error token', 'error_code': -1})
        except Exception as e:
            self.write({'success': 'fail', 'error': str(e), 'error_code': 500})
        if ver == True:
            pass




class user_data(BaseHandler):
    def post(self):
        print("/userdata")
        ver = False
        re = True
        try:
            post_data = self.request.body.decode('utf-8')
            print(post_data, type(post_data))
            post_data = json.loads(post_data)
            player = post_data["id"]
            usertoken = post_data["token"]

            try:
                user_data = post_data["data"]
                model = "user_data"
            except:
                model = "Password"

            v = tokens()
            v.set(player)
            ver = v.certify_token(usertoken)
            if ver == False:
                self.write({'success': 'fail', 'error': 'error token', 'error_code': -1})
        except Exception as e:
            self.write({'success': 'fail', 'error': str(e), 'error_code': 500})

        if ver == True:
            try:
                types="password"
                try:
                    name = Web3.toChecksumAddress(player)
                    types = "eth"
                    player = player.lower()
                except:
                    types = "password"
                    player = player.lower()

                db_table = str(player)[-2:]
                print(db_table,types)
                try:
                    int(db_table[0])
                    db_table = "a" + db_table
                except:
                    pass

                try:
                    if types == "password":
                        whois = 'select * from %s where user= "%s"' % (db_table, player)
                    else:
                        whois = 'select * from %s where eth_account= "%s"' % (db_table, player)
                    cur.execute(whois)
                    vip = cur.fetchall()
                    if vip != []:
                        pass
                    else:
                        self.write({'success': 'fail', 'data': 'no user ' + str(player),'error_code':-1})

                    if types == "eth":
                        verifya = funtion.verifyamessage(player, post_data["sign"])
                        if verifya == True:
                            # model = "user_data"
                            # model = "Password"
                            if model == "Password":
                                metadata = {'user': vip[0][0],
                                            'md5': post_data["new_password"],
                                            'user_name': vip[0][2],
                                            'email': vip[0][3],
                                            'eth_account': vip[0][4],
                                            'steem_id': vip[0][5],
                                            'invitedId': vip[0][6],
                                            'integral': vip[0][7],
                                            'token_num': vip[0][8],
                                            'lock_token': vip[0][9],
                                            'auth_info': vip[0][10],
                                            'spread_award_info': vip[0][11],
                                            'auction_info': vip[0][12],
                                            'buy_article': vip[0][13],
                                            'essay_info': vip[0][14],
                                            'countdown': vip[0][15],
                                            'prepare_info': vip[0][16],
                                            'goods': vip[0][17],
                                            'status': vip[0][18],
                                            'phone': vip[0][19],
                                            'avatar': vip[0][20],
                                            'activation': vip[0][21]}
                                q.put(["Password", metadata])
                                self.write({'success': 'ok'})
                            elif model == "user_data":
                                metadata = {'user': vip[0][0],
                                            'md5': vip[0][1],
                                            'user_name': vip[0][2],
                                            'email': vip[0][3],
                                            'eth_account': vip[0][4],
                                            'steem_id': vip[0][5],
                                            'invitedId': vip[0][6],
                                            'integral': vip[0][7],
                                            'token_num': vip[0][8],
                                            'lock_token': vip[0][9],
                                            'auth_info': vip[0][10],
                                            'spread_award_info': vip[0][11],
                                            'auction_info': vip[0][12],
                                            'buy_article': vip[0][13],
                                            'essay_info': vip[0][14],
                                            'countdown': vip[0][15],
                                            'prepare_info': vip[0][16],
                                            'goods': vip[0][17],
                                            'status': vip[0][18],
                                            'phone': vip[0][19],
                                            'avatar': vip[0][20],
                                            'activation': vip[0][21]}
                                for i in user_data:
                                    metadata[i] = user_data[i]
                                q.put(["user_data", metadata])
                                self.write({'success': 'ok'})
                        else:
                            self.write({'success': 'fail', 'error': 'error sign', 'error_code': -1})
                    elif types == "password":
                        try:
                            old_password = post_data["old_password"]
                        except:
                            old_password = post_data["password"]
                        if old_password == vip[0][1]:
                            if model == "Password":
                                metadata = {'user': vip[0][0],
                                            'md5': post_data["new_password"],
                                            'user_name': vip[0][2],
                                            'email': vip[0][3],
                                            'eth_account': vip[0][4],
                                            'steem_id': vip[0][5],
                                            'invitedId': vip[0][6],
                                            'integral': vip[0][7],
                                            'token_num': vip[0][8],
                                            'lock_token': vip[0][9],
                                            'auth_info': vip[0][10],
                                            'spread_award_info': vip[0][11],
                                            'auction_info': vip[0][12],
                                            'buy_article': vip[0][13],
                                            'essay_info': vip[0][14],
                                            'countdown': vip[0][15],
                                            'prepare_info': vip[0][16],
                                            'goods': vip[0][17],
                                            'status': vip[0][18],
                                            'phone': vip[0][19],
                                            'avatar': vip[0][20],
                                            'activation': vip[0][21]}
                                q.put(["Password", metadata])
                                self.write({'success': 'ok'})
                            elif model == "user_data":
                                metadata = {'user': vip[0][0],
                                            'md5': vip[0][1],
                                            'user_name': vip[0][2],
                                            'email': vip[0][3],
                                            'eth_account': vip[0][4],
                                            'steem_id': vip[0][5],
                                            'invitedId': vip[0][6],
                                            'integral': vip[0][7],
                                            'token_num': vip[0][8],
                                            'lock_token': vip[0][9],
                                            'auth_info': vip[0][10],
                                            'spread_award_info': vip[0][11],
                                            'auction_info': vip[0][12],
                                            'buy_article': vip[0][13],
                                            'essay_info': vip[0][14],
                                            'countdown': vip[0][15],
                                            'prepare_info': vip[0][16],
                                            'goods': vip[0][17],
                                            'status': vip[0][18],
                                            'phone': vip[0][19],
                                            'avatar': vip[0][20],
                                            'activation': vip[0][21]}
                                for i in user_data:
                                    metadata[i] = user_data[i]
                                q.put(["user_data", metadata])
                                self.write({'success': 'ok'})
                        else:
                            self.write({'success': 'fail', 'error': 'error password', 'error_code': -1})
                except Exception as e:
                    self.write({'success':'fail','error': str(e),'error_code':500})
            except Exception as e:
                self.write({'success':'fail','error': str(e),'error_code':500})


class user_message(BaseHandler):
    def post(self):
        print("/user")
        ip = self.request.headers.get("X-Real-Ip", "")
        ver = False
        re = True
        try:
            post_data = self.request.body.decode('utf-8')
            print(post_data, type(post_data))
            post_data = json.loads(post_data)
            player = post_data["id"]
            usertoken = post_data["token"]

            v=tokens()
            v.set(player)
            ver=v.certify_token(usertoken)
            if ver == False:
                self.write({'success': 'fail','error':'error token','error_code':-1})
        except Exception as e:
            self.write({'success': 'fail','error':str(e),'error_code':500})
        if ver == True:
            try:
                #player = self.get_argument('id')
                types="password"
                try:
                    name = Web3.toChecksumAddress(player)
                    types = "eth"
                    player = player.lower()
                except:
                    types = "password"
                    player = player.lower()

                db_table = str(player)[-2:]
                print(db_table,types)
                try:
                    int(db_table[0])
                    db_table = "a" + db_table
                except:
                    pass
                try:
                    if types == "password":
                        whois = 'select * from %s where user= "%s"' % (db_table, player)
                    else:
                        whois = 'select * from %s where eth_account= "%s"' % (db_table, player)
                    cur.execute(whois)
                    vip = cur.fetchall()
                    if vip != []:
                        metadata = {'user': vip[0][0],
                                    'user_name': vip[0][2],
                                    'email':vip[0][3],
                                    'eth_account': vip[0][4],
                                    'steem_id': vip[0][5],
                                    'invitedId': vip[0][6],
                                    'integral': vip[0][7],
                                    'token_num': vip[0][8],
                                    'lock_token': vip[0][9],
                                    'auth_info': vip[0][10],
                                    'spread_award_info': vip[0][11],
                                    'auction_info': vip[0][12],
                                    'buy_article': vip[0][13],
                                    'essay_info': vip[0][14],
                                    'countdown': vip[0][15],
                                    'prepare_info': vip[0][16],
                                    'goods': vip[0][17],
                                    'status': vip[0][18],
                                    'phone':vip[0][19],
                                    'avatar':vip[0][20],
                                    'activation':vip[0][21]}

                        self.write({'success': 'ok','data':metadata})
                    else:
                        try:
                            with open("ip.log", "r") as f:
                                allip = f.read()
                            if ip == "":
                                re = False
                                self.write({'success': 'fail', 'error': 'error ip', 'error_code': -1})
                                return
                            elif ip in allip:
                                re = False
                                self.write({'success': 'fail', 'error': 'ip has been registered in 24h','error_code':-1})
                                return
                        except Exception as e:
                            print(e)
                        if types == "eth" and re == True:
                            steem_id = "q" + funtion.md5(str(player).lower())[0:8]
                            redata = {'user': '', 'password': '', 'eth_account': player,'captcha': '', 'invitedId': ''}
                            q.put(["register", redata])
                            metadata = {'user': 'none',
                                        'user_name': 'none',
                                        'email': 'none',
                                        'eth_account': player,
                                        'steem_id': steem_id,
                                        'invitedId': 'none',
                                        'integral': 'none',
                                        'token_num': 'none',
                                        'lock_token': 'none',
                                        'auth_info': 'none',
                                        'spread_award_info': 'none',
                                        'auction_info': 'none',
                                        'buy_article': 'none',
                                        'essay_info': 'none',
                                        'countdown': 'none',
                                        'prepare_info': 'none',
                                        'goods': 'none',
                                        'status': 'none',
                                        'phone': 'none',
                                        'avatar': "none",
                                        'activation': "0"
                                        }
                            self.write({'success': 'ok', 'data': metadata})
                            with open("ip.log", "a") as file:
                                file.write(str(ip) + "\n")
                        else:
                            self.write({'success': 'fail','data':'no user ' + str(player),'error_code':-1})
                except Exception as e:
                    if "no such table" in str(e) and types == "eth":
                        try:
                            with open("ip.log", "r") as f:
                                allip = f.read()
                            if ip == "":
                                re = False
                                self.write({'success': 'fail', 'error': 'error ip', 'error_code': -1})
                                return
                            elif ip in allip:
                                re = False
                                self.write({'success': 'fail', 'error': 'ip has been registered in 24h','error_code':-1})
                                return
                        except Exception as e:
                            print(e)
                        if re == True:
                            steem_id = "q" + funtion.md5(str(player).lower())[0:8]
                            redata = {'user': '', 'password': '', 'eth_account': player, 'captcha': '', 'invitedId': ''}
                            q.put(["register", redata])
                            metadata = {'user': 'none',
                                        'user_name': 'none',
                                        'email': 'none',
                                        'eth_account': player,
                                        'steem_id': steem_id,
                                        'invitedId': 'none',
                                        'integral': 'none',
                                        'token_num': 'none',
                                        'lock_token': 'none',
                                        'auth_info': 'none',
                                        'spread_award_info': 'none',
                                        'auction_info': 'none',
                                        'buy_article': 'none',
                                        'essay_info': 'none',
                                        'countdown': 'none',
                                        'prepare_info': 'none',
                                        'goods': 'none',
                                        'status': 'none',
                                        'phone': 'none',
                                        'avatar': "none",
                                        'activation': "0"
                                        }
                            self.write({'success': 'ok', 'data': metadata})
                            with open("ip.log", "a") as file:
                                file.write(str(ip) + "\n")
                    else:
                        self.write({'success': 'fail','error':str(e),'error_code':500})
            except Exception as e:
                self.write({'success':'fail','error': str(e),'error_code':500})


class login(BaseHandler):
    def post(self):
        try:
            print("/login")
            post_data = self.request.body.decode('utf-8')
            print(post_data,type(post_data))
            post_data = json.loads(post_data)
            types = post_data["type"]
            data = post_data["data"]
            print(types,data)
            if types == "eth":
                verifya = funtion.verifyamessage(data[0], data[1])
                if verifya == True:
                    v = tokens()
                    v.set(data[0])
                    usertoken = v.generate_token(3600 * 24 * 7)
                    self.write({'success':'ok','token':usertoken})

                else:
                    self.write({'success':'fail','error':'error sign','error_code':-1})
            elif types == "password":


                db_table = "none"
                player = data[0]
                password = data[1]
                db_table = str(player)[-2:]
                try:
                    int(db_table[0])
                    db_table = "a" + db_table
                except:
                    pass
                try:
                    whois = 'select * from %s where user= "%s"' % (db_table, player)
                    cur.execute(whois)
                    vip = cur.fetchall()
                    print(vip)
                    if vip == []:
                        self.write({'success': 'fail', 'error': 'no user','error_code':-1})
                    else:
                        if vip[0][1] == password:
                            v = tokens()
                            v.set(data[0])
                            usertoken = v.generate_token(3600 * 24 * 7)
                            self.write({'success': 'ok', 'token': usertoken})
                        else:
                            self.write({'success': 'fail', 'error': 'error password','error_code':-1})
                except Exception as e:
                    self.write({'success':'fail','error':str(e),'error_code':500})

        except Exception as e:
            self.write({'success':'fail','error':str(e),'error_code':500})

class register(BaseHandler):
    def post(self):
        print("/register")
        re = True
        ip = self.request.headers.get("X-Real-Ip", "")
        print("ip",ip)

        with open("ip.log", "r") as f:
            allip = f.read()
        if ip == "":
            re = False
            self.write({'success': 'fail', 'error': 'error ip', 'error_code': -1})
            return
        elif ip in allip:
            re = False
            self.write({'success': 'fail', 'error': 'ip has been registered in 24h','error_code':-1})
            return
        if re == True:
            try:
                black = False
                post_data = self.request.body.decode('utf-8')
                print(post_data,type(post_data))
                post_data = json.loads(post_data)
                redata = {'user': post_data["user"], 'password': post_data["password"], 'eth_account': '', 'captcha': post_data["captcha"], 'invitedId': post_data["invitedId"]}
                black_name = ["null", "none", "None"]
                if post_data["user"] in black_name:
                    black = True
                black_name2 = ["\"", "\\", "/", "|", "&", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", "$","(", ")", "%", "@", "!"]
                for i in black_name2:
                    if i in post_data["user"]:
                        black = True
                if len(post_data["user"]) > 16 or len(post_data["user"]) < 4 or black == True:
                    self.write({'success':'fail','error':'error username','error_code':-1})
                else:
                    try:
                        player = post_data["user"]
                        db_table = str(player)[-2:]
                        try:
                            int(db_table[0])
                            db_table = "a" + db_table
                        except:
                            pass
                        whois = 'select * from %s where user= "%s"' % (db_table, player)
                        cur.execute(whois)
                        vip = cur.fetchall()
                        if vip != []:
                            self.write({'success': 'fail', 'error': 'user has been registered','error_code':-1})
                        else:
                            q.put(["register",redata])
                            self.write({'success': 'ok', 'data': redata})
                            with open("ip.log", "a") as file:
                                file.write(str(ip) + "\n")
                    except Exception as e:
                        if "no such table" in str(e):
                            q.put(["register", redata])
                            self.write({'success': 'ok', 'data': redata})
                            with open("ip.log", "a") as file:
                                file.write(str(ip) + "\n")
                        else:
                            self.write({'success': 'fail', 'error': str(e),'error_code':500})
            except Exception as e:
                self.write({'success':'fail','error':str(e),'error_code':500})

def make_app():
    return tornado.web.Application([(r"/", MainHandler),(r"/user", user_message),(r"/login", login),(r"/register", register),(r"/password", user_data),(r"/userdata", user_data),(r"/subscriptions", quan),])

def print_queue(threadName):
    while True:
        if not q.empty():
            s=q.get()
            if s[0] == "register":
                player=s[1]["user"]
                if player == '':
                    player = "none"
                password = s[1]["password"]
                if password == '':
                    password = "none"
                eth_account = s[1]["eth_account"]
                if eth_account == '':
                    eth_account = "none"
                invitedId = s[1]["invitedId"]
                if invitedId == '':
                    invitedId = "none"

                funtion.new(player,password,eth_account,invitedId)
            elif s[0] == "Password":
                funtion.Password(s[1])
            elif s[0] == "user_data":
                funtion.Password(s[1])
            elif s[0] == "quan_join":
                funtion.join("+",s[1][0],s[1][1])

def quan_queue(threadName):
    while True:
        if not q2.empty():
            s=q2.get()
            if s[0] == "create_quan":
                funtion.Create_quan(s[1])

def clean_ip(threadName):
    while True:
        time.sleep(3600*24)
        file = open("ip.log", 'w').close()

_thread.start_new_thread(print_queue, ("Thread-1", ))
_thread.start_new_thread(quan_queue, ("Thread-2", ))
_thread.start_new_thread(clean_ip, ("clean_ip-1", ))

if __name__ == "__main__":

    app = make_app()

    app.listen(7858,xheaders = True)

    tornado.ioloop.IOLoop.current().start()
