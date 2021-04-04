@REM python genGrid.py > input.txt ^
@REM && echo. ^
@REM  && echo ------------- GBFS ------------- ^
@REM  && type input.txt | python GBFS.py ^
@REM && echo. ^
@REM  && echo ------------- AStar ------------- ^
@REM  && type input.txt | python AStar.py

echo. ^
 && type input.txt | python GBFS.py > GBFS_output.txt ^
&& echo. ^
 && type input.txt | python AStar.py > AStar_output.txt