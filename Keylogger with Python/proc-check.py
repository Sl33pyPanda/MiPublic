import psutil

PROCNAME = ['Unikey',
            'unikey',
            'UniKey',
            'uniKey']

for proc in psutil.process_iter():
#    print(proc.name())
    for p in PROCNAME:
        if p in proc.name():
            return True

