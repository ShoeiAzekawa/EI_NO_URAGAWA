from fastapi import FastAPI, Request,File,UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn
import shutil
import os

#ID
count = 1
#インスタンス化(空箱)
app = FastAPI()
#cssファイルを使用するようにできる
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/image", StaticFiles(directory="image"), name="image")

#Jinja2テンプレートエンジンを使用するための設定
templates = Jinja2Templates(directory="templates")
#image = Jinja2Templates(directory="image")

""" HTTPメソッド """
""" /は、一番メインのURLにアクセスがあったらという意味 """
""" 22行目の処理でドメイン名を呼び出している """
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("templates.html",{
        "request": request
    })

@app.post("/upload_file")
#UploadFileはアップロードされたファイルに関する情報を保持する。
async def upload_file(my_file: UploadFile, request: Request):
    #ファイルのアップロード先を指定、./filesフォルダに新しいファイルが保存される。
    upload_dir = open(os.path.join("./files", my_file.filename), "wb+")
    #アップロードされたファイルのデータを新しいファイルにコピー
    shutil.copyfileobj(my_file.file, upload_dir)
    upload_dir.close()
    return templates.TemplateResponse("send.html",{
        "request": request
    })




