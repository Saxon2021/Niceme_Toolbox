### 强制覆盖远程代码

```gitignore
git push -f --set-upstream origin master:master
```

### 强制覆盖本地代码

```gitignore
git fetch --all
git reset --hard origin/master
git pull

git fetch --all &&  git reset --hard origin/master && git pull
```

### 提交代码操作

```gitignore
git add *
git commit -m "备注"
git push origin master
```

### 拉取远程代码

```gitignore
git pull origin master
```

### Git远程仓库地址

```gitignore
https://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@github.com/Saxon2021/Niceme_Client.git
```

### 生成requirements文件

```gitignore
pip freeze > ./requirements.txt
```

### 安装requirements文件

```gitignore
pip install -r ./codes/requirements.txt
pip install -r E:\Anireel_Code\Anireel_Pack\requirements.txt
```