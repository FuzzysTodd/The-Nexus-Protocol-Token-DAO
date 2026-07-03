import wx
from _typeshed import Incomplete

def ignore_keyboardinterrupts(func):
    """Decorator which causes KeyboardInterrupt exceptions to be ignored during
    execution of the decorated function.

    This is used by the inputhook functions to handle the event where the user
    presses CTRL+C while IPython is idle, and the inputhook loop is running. In
    this case, we want to ignore interrupts.
    """
def inputhook_wx1(context):
    """Run the wx event loop by processing pending events only.

    This approach seems to work, but its performance is not great as it
    relies on having PyOS_InputHook called regularly.
    """

class EventLoopTimer(wx.Timer):
    func: Incomplete
    def __init__(self, func) -> None: ...
    def Notify(self) -> None: ...

class EventLoopRunner:
    input_is_ready: Incomplete
    evtloop: Incomplete
    timer: Incomplete
    def Run(self, time, input_is_ready) -> None: ...
    def check_stdin(self) -> None: ...

def inputhook_wx2(context):
    """Run the wx event loop, polling for stdin.

    This version runs the wx eventloop for an undetermined amount of time,
    during which it periodically checks to see if anything is ready on
    stdin.  If anything is ready on stdin, the event loop exits.

    The argument to elr.Run controls how often the event loop looks at stdin.
    This determines the responsiveness at the keyboard.  A setting of 1000
    enables a user to type at most 1 char per second.  I have found that a
    setting of 10 gives good keyboard response.  We can shorten it further,
    but eventually performance would suffer from calling select/kbhit too
    often.
    """
def inputhook_wx3(context):
    """Run the wx event loop by processing pending events only.

    This is like inputhook_wx1, but it keeps processing pending events
    until stdin is ready.  After processing all pending events, a call to
    time.sleep is inserted.  This is needed, otherwise, CPU usage is at 100%.
    This sleep time should be tuned though for best performance.
    """
def inputhook_wxphoenix(context) -> None:
    """Run the wx event loop until the user provides more input.

    This input hook is suitable for use with wxPython >= 4 (a.k.a. Phoenix).

    It uses the same approach to that used in
    ipykernel.eventloops.loop_wx. The wx.MainLoop is executed, and a wx.Timer
    is used to periodically poll the context for input. As soon as input is
    ready, the wx.MainLoop is stopped.
    """

major_version: int
inputhook = inputhook_wxphoenix
inputhook = inputhook_wx3
