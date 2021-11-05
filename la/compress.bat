@echo OFF
SET subject=%*
for %%a in (%*) do set subject=%%a
python C:\\Users\\Max\\ffmpeg-compress\\compress.py %subject%