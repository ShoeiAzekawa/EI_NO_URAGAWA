from fastapi import FastAPI, Request,File,UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn
import shutil
import os

#インスタンス化(空箱)
app = FastAPI()
#cssファイルを使用するようにできる
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/image", StaticFiles(directory="image"), name="image")
app.mount("/result", StaticFiles(directory="result"), name="result")

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
    
@app.get("/image")
async def index(imageID: str, request: Request):
    
    """#ファイル数を数えている
    dir = "./result"
    #ディレクトリの中身分ループ
    for file_name in os.listdir(dir):
        #ファイルもしくはディレクトリのパスを取得
        file_path = os.path.join(dir,file_name)
        #ファイルであるか判定
        if os.path.isfile(file_path):
            if imageID == "desired_filename":"""
    return templates.TemplateResponse("name.html",{
        "imageID": imageID,
        "request": request
    })    

@app.post("/upload_file")
#UploadFileはアップロードされたファイルに関する情報を保持する。
async def upload_file(my_file: UploadFile, request: Request):
    #ファイル数を数えている
    dir = "./files"
    count_file = 1
    #ディレクトリの中身分ループ
    for file_name in os.listdir(dir):
        #ファイルもしくはディレクトリのパスを取得
        file_path = os.path.join(dir,file_name)
        #ファイルであるか判定
        if os.path.isfile(file_path):
            count_file +=1
            
    id = str(count_file) + ".jpg"
    filename = id
    #ファイルのアップロード先を指定、./filesフォルダに新しいファイルが保存される。
    upload_dir = open(os.path.join("./files", filename), "wb+")
    #アップロードされたファイルのデータを新しいファイルにコピー
    shutil.copyfileobj(my_file.file, upload_dir)
    upload_dir.close()
    
    return templates.TemplateResponse("send.html",{
        "count_file" : count_file,
        "request": request
    })




