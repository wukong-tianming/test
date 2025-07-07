ONLINE_DOWNLOAD_SOURCES = [
    # 直接下载ZIP格式（优先）
    "https://furcate.eu/FILES/{appid}.zip",
    "https://steamdatabase.s3.eu-north-1.amazonaws.com/{appid}.zip",

    # GitHub仓库路径（使用CDN代理）
    {"githubcangku": {
        "ManifestHub": "SteamAutoCracks/ManifestHub"   ,
        "Auiowu/ManifestAutoUpdate": "Auiowu/ManifestAutoUpdate", 
        "ManifestAutoUpdate-fix": "tymolu233/ManifestAutoUpdate-fix"
    }}
]