#!/usr/bin/env bash

yes | ffmpeg -i anim/%d.png -c:v libx264 -vf "fps=25,format=yuv420p" 12gon.mp4
