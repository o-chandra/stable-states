#Model from the 2003 paper "EFFECTS OF FIRE AND HERBIVORY ON THE STABILITY OF SAVANNA ECOSYSTEMS"

#Define parameters
u=0.6;
rh=1.0;
rw=0.5;
dh=0.9; dw=0.4;
alpha=0.4;
beta=300;
p=1;
kh=0.1; #fire parameters are set to 0 in simplified model below
kw=0.01;
n=0.1;
a=0.5;

#Define rate of moisture recharge functions. Doing this for three scenarios
#Scenario A: w_in=250 < beta
#Scenario B: w_in=500 > beta
#Scenario C: w_in =750 >> beta

##set the scenario below##
def set_scenario(scenario):
    if (scenario=="A"):
        win=250
    elif (scenario=="B"):
        win=500
    elif (scenario=="C"):
        win=700
    else:
        return("Invalid scenario designation")

def ws(alpha,beta,win):
    if win>beta:
        return alpha*(win-beta)
    else:
        return 0
