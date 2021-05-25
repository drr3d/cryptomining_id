@ECHO OFF
: Sets the proper date Time for log file naming
: Sets required param that used for mining

set datetimef=%date:~-4%_%date:~3,2%_%date:~0,2%

@ECHO OFF
: Main Settings
set mininguser=yourwalletaddress_here.your_rigalias_here
set miningport=12020
set miningserver=asia-eth.2miners.com
set miningalgo=ethash
set miningbakserver=eth.2miners.com

@ECHO OFF
: Additional Settings
set mininglog= %datetimef%_miner.log
set miningwdog=1
set miningnvml=1
set miningcuda=1
set miningopencl=0

@ECHO OFF
: Delete same name file first, to make it clear log
IF EXIST %mininglog%. (
    del %mininglog%.
) 

@ECHO OFF
: Change directory to where u put the miner.exe of GMiner, Admin privilages need this
set miner_dir="C:\your_mining_directory_here"
cd %miner_dir%

miner.exe --algo %miningalgo% --server %miningserver%  --port %miningport% --user %mininguser% --ssl 1 --server %miningbakserver%  --port %miningport% --user %mininguser%  -d 0 1 --opencl 0 --templimit 70 --ssl 1 --api 10555 --p2state 0 --logfile %mininglog%
pause


