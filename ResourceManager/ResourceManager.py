import os
import binascii


NODES = [[],
         [],
         [],
         [["'[b]1.click'", "'[b]4.click'"],["'[b]2.click'","'[b]5.click'"],["'[b]6.click'","'[b]7.click'"]],
         [["'[b]8.click'", "'[b]9.click'"]],
         [["'[b]10.click'","'[b]3.click'"]]]


router_commands = {
    "'[b]1.click'": 'click EXTROUTE=b1-eth2 INTROUTE1=b1-eth1 Routers/b1.click > "Routers/Logs/b1.log" 2>&1 &',
    "'[b]2.click'": 'click EXTROUTE=b2-eth2 INTROUTE1=b2-eth1 Routers/b2.click > "Routers/Logs/b2.log" 2>&1 &',
    "'[b]3.click'": 'click EXTROUTE=b3-eth2 INTROUTE1=b3-eth1 Routers/b3.click > "Routers/Logs/b3.log" 2>&1 &',
    "'[b]4.click'": 'click EXTROUTE=b4-eth2 INTROUTE1=b4-eth1 Routers/b4.click > "Routers/Logs/b4.log" 2>&1 &',
    "'[b]5.click'": 'click EXTROUTE=b5-eth2 INTROUTE1=b5-eth1 Routers/b5.click > "Routers/Logs/b5.log" 2>&1 &',
    "'[b]6.click'": 'click EXTROUTE=b6-eth2 INTROUTE1=b6-eth1 Routers/b6.click > "Routers/Logs/b6.log" 2>&1 &',
    "'[b]7.click'": 'click EXTROUTE=b7-eth2 INTROUTE1=b7-eth1 Routers/b7.click > "Routers/Logs/b7.log" 2>&1 &',
    "'[b]8.click'": 'click EXTROUTE=b8-eth2 INTROUTE1=b8-eth1 Routers/b8.click > "Routers/Logs/b8.log" 2>&1 &',
    "'[b]9.click'": 'click EXTROUTE=b9-eth2 INTROUTE1=b9-eth1 Routers/b9.click > "Routers/Logs/b9.log" 2>&1 &',
    "'[b]10.click'":'click EXTROUTE=b10-eth2 INTROUTE1=b10-eth1 Routers/b10.click > "Routers/Logs/b10.log" 2>&1 &'
}


class ResourceManager:

    def getProcessID(self, processName):
        command  = "ps aux | grep " + processName + " | awk '{print $2}' > PID.txt"
        os.system(command)
        with open('PID.txt','r') as f:
            processID = f.readline()
        processID = processID.replace('\n','')
        os.system('rm -f PID.txt')
        return processID
    
    def killProcess(self, processName):
        processID = self.getProcessID(processName)
        if len(processID)>1:
            command = 'kill '+ processID
            # print(command)
            os.system(command)
        else:
            print('Process not executing')

    def updateRouter(self, processName):
        self.killProcess(processName)
        os.system(router_commands[processName])


    def updatePublicPID(self, fileName, value):
        configuration = []
        with open(fileName, 'r') as f:
            configuration = f.readlines()
        line = configuration[5]
        configuration[5] = line[:36]+value+line[37:]
        with open(fileName, 'w') as f:
            f.write(''.join(configuration))


    def updatePrivatePID(self, fileName, value):
        configuration = []
        value = str(binascii.b2a_hex(bytes(str(value))))
        with open(fileName, 'r') as f:
            configuration = f.readlines()
        line = configuration[7]
        configuration[7] = line[:48]+value+line[50:]
        with open(fileName, 'w') as f:
            f.write(''.join(configuration))

    def updatePID(self, RMID, values):
        RM_NODES = NODES[RMID-1]
        for node in RM_NODES:
            value = values.pop(0)
            path = 'Routers/'
            node_1 = node[0].replace('[b]','b').strip("'")
            node_2 = node[1].replace('[b]','b').strip("'")
            self.updatePublicPID( path + node_1, value)
            self.updatePrivatePID(path + node_2, value)
            self.updateRouter(node[0])
            self.updateRouter(node[1])
        


# if __name__ == "__main__":

#     RM = ResourceManager(4)
#     RM.killProcess(NODES[3][0][1])

