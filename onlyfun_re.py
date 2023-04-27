import tornado.ioloop
import tornado.web
import tornado.httpclient

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        url = "http://45.77.114.109:668" + self.request.uri
        headers = self.request.headers
        headers["X-Real-IP"] = self.request.remote_ip
        response = await tornado.httpclient.AsyncHTTPClient().fetch(url, headers=headers)
        self.write(response.body)

    async def post(self):
        url = "http://45.77.114.109:668" + self.request.uri
        headers = self.request.headers
        headers["X-Real-IP"] = self.request.remote_ip
        response = await tornado.httpclient.AsyncHTTPClient().fetch(url, method="POST", body=self.request.body, headers=headers)
        self.write(response.body)

    async def put(self):
        url = "http://45.77.114.109:668" + self.request.uri
        headers = self.request.headers
        headers["X-Real-IP"] = self.request.remote_ip
        response = await tornado.httpclient.AsyncHTTPClient().fetch(url, method="PUT", body=self.request.body, headers=headers)
        self.write(response.body)

    async def delete(self):
        url = "http://45.77.114.109:668" + self.request.uri
        headers = self.request.headers
        headers["X-Real-IP"] = self.request.remote_ip
        response = await tornado.httpclient.AsyncHTTPClient().fetch(url, method="DELETE", headers=headers)
        self.write(response.body)

def make_app():
    return tornado.web.Application([
        (r"/.*", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(668)
    tornado.ioloop.IOLoop.current().start()