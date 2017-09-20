import subprocess


def _osascript(script):
    """
    Execute AppleScript.
    """
    return subprocess.run(
        ['osascript', '-e', str(script)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


def vol_mute():
    """
    Grab the current volume status and mute/unmute accordingly.

    `muted.stdout` gives us the output from `_osascript()` in bytes. We decode
    it to UTF-8 and strip any trailing whitespaces. The end result is a string:
    `true` if volume is muted, `false` if not.
    """
    muted = _osascript('output muted of (get volume settings)')
    muted = muted.stdout.decode('utf-8').rstrip()

    if muted == 'false':
        _osascript('set volume output muted true')
        return 'System volume has been muted.'
    elif muted == 'true':
        _osascript('set volume output muted false')
        return 'System volume has been unmuted.'


def vol_set(level):
    """
    Set volume to `level`.
    """
    if 0 <= int(level) <= 100:
        _osascript('set volume output volume {}'.format(level))
        return 'System volume set to {}.'.format(level)
    return 'Volume level must be between 0 and 100.'


def display_brightness(level):
    """
    Set display brightness to `level`.
    """
    if 0 <= int(level) <= 100:
        # `brightness` expects the level to be between 0.1 ~ 1.0, we'll convert
        # it to such and cast it to string for `subprocess.run()`.
        subprocess.run(
            ['brightness', str(int(level)/100)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return 'Display brightness set to {}.'.format(level)
    return 'Brightness level must be between 0 and 100.'


def display_sleep():
    """
    Put the display to sleep.
    """
    subprocess.run(
        ['pmset', 'displaysleepnow'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return 'Display has been put to sleep.'
