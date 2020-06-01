import sys

import frida


def on_message(message, data):
    print(message)


js_code = """
    Process.enumerateModules({
          onMatch:function(exp){
        send(exp.name);
      },
          onComplete:function(){
        send("stop");
      }
})
"""
process = frida.get_usb_device().attach('com.wondertek.paper')
script = process.create_script(js_code)
script.on('message', on_message)
script.load()
sys.stdin.read()
