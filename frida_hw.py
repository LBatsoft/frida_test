import frida


remote_dev = frida.get_remote_device()
print(remote_dev)
front_app = remote_dev.get_frontmost_application()
print(front_app)

process = remote_dev.enumerate_processes()
for i in process:
    print(i)