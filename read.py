ONLINE_DOWNLOAD_SOURCES = [
    # 直接下载ZIP格式（优先）
    "https://furcate.eu/FILES/{appid}.zip",
    "https://assiw.cngames.site/qindan/{app_id}.zip",
    "https://steamdatabase.s3.eu-north-1.amazonaws.com/{appid}.zip",
    "https://cysaw.top/uploads/{app_id}.zip",

    # GitHub仓库路径（使用CDN代理）
    {"githubcangku": {
        "ManifestHub": "SteamAutoCracks/ManifestHub"   ,
        "Auiowu/ManifestAutoUpdate": "Auiowu/ManifestAutoUpdate", 
        "ManifestAutoUpdate-fix": "tymolu233/ManifestAutoUpdate-fix"
    }}
]