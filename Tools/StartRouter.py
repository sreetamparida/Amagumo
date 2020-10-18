import os

ROUTER_COMMANDS = {
    'r1.click' : 'click EXTROUTE=r1-eth3 INTROUTE2=r1-eth2 INTROUTE1=r1-eth1 Routers/r1.click > "Routers/Logs/r1.log" 2>&1 &',
    'r4.click' : 'click EXTROUTE=r4-eth3 INTROUTE2=r4-eth2 INTROUTE1=r4-eth1 Routers/r4.click > "Routers/Logs/r4.log" 2>&1 &',
    'r2.click' : 'click EXTROUTE=r2-eth2 INTROUTE1=r2-eth1 Routers/r2.click > "Routers/Logs/r2.log" 2>&1 &',
    'r3.click' : 'click EXTROUTE=r3-eth2 INTROUTE1=r3-eth1 Routers/r3.click > "Routers/Logs/r3.log" 2>&1 &',
    'r5.click' : 'click EXTROUTE=r5-eth2 INTROUTE1=r5-eth1 Routers/r5.click > "Routers/Logs/r5.log" 2>&1 &',
    'r6.click' : 'click EXTROUTE=r6-eth2 INTROUTE1=r6-eth1 Routers/r6.click > "Routers/Logs/r6.log" 2>&1 &',
    'b1.click' : 'click EXTROUTE=b1-eth2 INTROUTE1=b1-eth1 Routers/b1.click > "Routers/Logs/b1.log" 2>&1 &',
    'b2.click' : 'click EXTROUTE=b2-eth2 INTROUTE1=b2-eth1 Routers/b2.click > "Routers/Logs/b2.log" 2>&1 &',
    'b3.click' : 'click EXTROUTE=b3-eth2 INTROUTE1=b3-eth1 Routers/b3.click > "Routers/Logs/b3.log" 2>&1 &',
    'b4.click' : 'click EXTROUTE=b4-eth2 INTROUTE1=b4-eth1 Routers/b4.click > "Routers/Logs/b4.log" 2>&1 &',
    'b5.click' : 'click EXTROUTE=b5-eth2 INTROUTE1=b5-eth1 Routers/b5.click > "Routers/Logs/b5.log" 2>&1 &',
    'b6.click' : 'click EXTROUTE=b6-eth2 INTROUTE1=b6-eth1 Routers/b6.click > "Routers/Logs/b6.log" 2>&1 &',
    'b7.click' : 'click EXTROUTE=b7-eth2 INTROUTE1=b7-eth1 Routers/b7.click > "Routers/Logs/b7.log" 2>&1 &',
    'b8.click' : 'click EXTROUTE=b8-eth2 INTROUTE1=b8-eth1 Routers/b8.click > "Routers/Logs/b8.log" 2>&1 &',
    'b9.click' : 'click EXTROUTE=b9-eth2 INTROUTE1=b9-eth1 Routers/b9.click > "Routers/Logs/b9.log" 2>&1 &',
    'b10.click':'click EXTROUTE=b10-eth2 INTROUTE1=b10-eth1 Routers/b10.click > "Routers/Logs/b10.log" 2>&1 &'
}

def startRouter(routerName):
    print('Executing command')
    print(ROUTER_COMMANDS[routerName])
    os.system(ROUTER_COMMANDS[routerName])