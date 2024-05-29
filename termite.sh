# bash version of Termite Crediential Hunter
# Made with love
# 2xdropout 2024

# Text Coloring
HEADER='\033[95m'
OKBLUE='\033[94m'
OKCYAN='\033[96m'
OKGREEN='\033[92m'
WARNING='\033[93m'
FAIL='\033[91m'
ENDC='\033[0m'
BOLD='\033[1m'
UNDERLINE='\033[4m'
BU=BOLD+UNDERLINE


function draw_logo(){
	printf "${OKGREEN}--------------------------------------------------------------\n"
	printf "|                                                            |\n"
	printf "|  ████████╗███████╗██████╗ ███╗   ███╗██╗████████╗███████╗  |\n"
	printf "|  ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║╚══██╔══╝██╔════╝  |\n"
	printf "|     ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║   █████╗    |\n"
	printf "|     ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║   ██╔══╝    |\n"
	printf "|     ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║   ██║   ███████╗  |\n"
	printf "|     ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   ╚══════╝  |\n"
	printf "${OKGREEN}--------------------------------------------------------------${ENDC}\n"
}


function main(){
	draw_logo
}


main

