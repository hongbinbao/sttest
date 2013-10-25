from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as de
from com.android.monkeyrunner import MonkeyImage as mi
d = mr.waitForConnection()
d.startActivity(component='com.android.settings/.Settings')
print d.shell('ps')

