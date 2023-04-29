import tornado.ioloop
import tornado.web
import tornado.httpclient
import configparser
import random



config = configparser.ConfigParser()
config.read('config_node.ini')

api_url = config.get('api', 'key1')
nodes = config.get('node', 'key1')

class MainHandler(tornado.web.RequestHandler):


    async def get(self):
        url = api_url + self.request.uri +'?rand=' + str(random.random())
        print("get")
        print(url)
        self.set_header('Cache-Control', 'no-store')
        headers = self.request.headers
        headers["X-Real-IP"] = self.request.headers.get("X-Real-IP", self.request.remote_ip)
        request = tornado.httpclient.HTTPRequest(url, method="GET", headers=headers, validate_cert=False)
        response = await tornado.httpclient.AsyncHTTPClient().fetch(request)
        self.write(response.body)

    async def post(self):
        post_data = self.request.body.decode('utf-8')
        print(post_data)
        if 'jsonrpc' in post_data:
            url = nodes
        else:
            request_uri = self.request.uri
            if "/api" in request_uri:
                print(request_uri,type(request_uri))
                request_uri.replace("/api","")
            url = api_url + self.request.uri
        print(url)
        headers = self.request.headers
        headers["X-Real-IP"] = self.request.headers.get("X-Real-IP", self.request.remote_ip)
        request = tornado.httpclient.HTTPRequest(url, method="POST", body=self.request.body, headers=headers, validate_cert=False)
        response = await tornado.httpclient.AsyncHTTPClient().fetch(request)
        self.write(response.body)

    async def put(self):
        post_data = self.request.body.decode('utf-8')
        if 'jsonrpc' in post_data:
            url = nodes
        else:
            url = api_url + self.request.uri
        headers = self.request.headers
        headers["X-Real-IP"] = self.request.headers.get("X-Real-IP", self.request.remote_ip)
        request = tornado.httpclient.HTTPRequest(url, method="PUT", body=self.request.body, headers=headers, validate_cert=False)
        response = await tornado.httpclient.AsyncHTTPClient().fetch(request)
        self.write(response.body)

    async def delete(self):
        post_data = self.request.body.decode('utf-8')
        if 'jsonrpc' in post_data:
            url = nodes
        else:
            url = api_url + self.request.uri
        headers = self.request.headers
        headers["X-Real-IP"] = self.request.headers.get("X-Real-IP", self.request.remote_ip)
        request = tornado.httpclient.HTTPRequest(url, method="DELETE", headers=headers, validate_cert=False)
        response = await tornado.httpclient.AsyncHTTPClient().fetch(request)
        self.write(response.body)

def make_app():
    return tornado.web.Application([
        (r"/.*", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(669)
    tornado.ioloop.IOLoop.current().start()