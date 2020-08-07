import frida
import sys

device = frida.get_remote_device()
session = device.attach("com.yixia.videoeditor")

scr = """
setImmediate(function() {
Interceptor.attach(Module.findExportByName("libte.so" , "sign"), {
    onEnter: function(args) {

        send("gifcore so args: "args[0]+", "+args[1]+", "+args[2]+", "+args[3]+","+args[4]);
    },
    onLeave:function(retval){
        send("gifcore so result value: "+retval);
    }
});

});
"""

script = session.create_script(scr)
def on_message(message, data):
    print(message)
    print(data)

script.on("message", on_message)
script.load()
sys.stdin.read()