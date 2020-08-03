import frida
import sys
jscode ='''
Java.perform(function(){
    var SnsUploadUI = Java.use('com.tencent.mm.plugin.sns.ui.SnsUploadUI');
    var ai = SnsUploadUI.ai.overload("android.os.Bundle");
    ai.implementation = function(bundle)
    {
    var ret = ai.call(this, bundle);
    send("sns type = " + this.wUl.value);
    return ret;
    }
}
);
'''
def message(message,data):
    if message["type"] == 'send':
        print("[*] {0}".format(message["payload"]))
    else:
        print(message)

process = frida.get_remote_device().attach("com.tencent.mm")
script = process.create_script(jscode)
script.on("message",message)
script.load()
sys.stdin.read()
