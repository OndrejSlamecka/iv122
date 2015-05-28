#!/usr/bin/env bash

yes | ffmpeg -i julia_anim/%d.png -c:v libx264 -vf "fps=25,format=yuv420p" julia.mp4
