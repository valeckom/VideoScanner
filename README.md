# VideoScanner

NAME
        videoScanner.py - checks the integrity of video files in a directory

SYNOPSIS
        python videoScanner.py [OPTION] [DIRECTORY]

DEPENDENCIES
        ffmpeg must be installed in order to function
        install it using:
        $ apt install ffmpeg

DESCRIPTION
        Scan all video files in a directory. Log the first error in the video file.       

    Exit status:
        0       if OK

        1       if there is an input error

COMMAND-LINE OPTIONS
        The default behavior of videoScanner will scan all video files within a directory.
        When the first error is found it is logged and the scanner moves onto the next file.

        -w      scan the whole file. This will log all errors found in each video file

        -n      scan (new) files; that have not been scanned previously

EXAMPLE USAGE
        $ python videoScanner.py ~/Desktop/videos/
                Scan all videos in the videos folder on the desktop. The results will
                be logged in the video_scanner.log file inside of the same folder.

        $ python videoScanner.py -w ~/Desktop/videos/
                Scan all videos in the videos folder on the desktop. The results will
                be logged in the video_scanner.log file inside of the same folder.

AUTHOR
        Written by Mark Valecko

COPYRIGHT
        MIT License

        Copyright (c) 2018 valeckom

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
