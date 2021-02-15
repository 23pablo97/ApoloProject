import speedtest

servers = []
threads = None

def calculate_speedtest():
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    res = s.results.dict()
    res['download'] = int(res['download']/1000000)
    res['upload'] = int(res['upload']/1000000)
    return res
