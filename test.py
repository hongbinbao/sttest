print 'monkeyrunner testing'
from com.android.monkeyruner import MonkeyRunner as m
from com.android.monkeyruner import MonkeyDevice as d
d = m.waitForConnection()
d.wake()
print '1234456'

