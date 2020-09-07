import Instructions
import Registers 
import MainMemory

#Contains all the components of IAS machines
class Computer():
    def __init__(self):
        self.registers=Registers.Registers()
        self.memory=MainMemory.MainMemory()    
        self.instructions=Instructions.INSTRUCTIONS()  

#performs fetch operation
def Fetch(address,IAS):
    IAS.registers.MAR = IAS.registers.PC
    IAS.registers.MAR = Instructions.convert_DecToBin(address)
    IAS.registers.MBR = IAS.memory.mem[Instructions.convert_ListToDec(IAS.registers.MAR)]
      
    if(IAS.registers.IBR == [0]*20):
        IAS.registers.IBR = IAS.registers.MBR[20:]
        IAS.registers.IR = IAS.registers.MBR[0:8]
        IAS.registers.MAR = IAS.registers.MBR[8:20]
        
    else:
        IAS.registers.IR = IAS.registers.IBR[0:8]
        IAS.registers.MAR = IAS.registers.IBR[8:]
        IAS.registers.IBR =[0]*20    
        IAS.registers.PC+=1
           
                
def verify(operation):
    if(operation.__name__ == "JUMP_MX_LHS" ):
        return True
    if(operation.__name__ == "JUMP_MX_RHS"):
        return True 
    if(operation.__name__ == "JUMP_CONDITIONAL_MX_LHS"):
        return True
    if( operation.__name__ == "JUMP_CONDITIONAL_MX_RHS"):
        return True     
    return False    

#executes the operation
def Execute(address,IAS,tempo):
    operation = IAS.instructions.opcodesCheck(IAS.registers.IR)

    if(operation!=False):
        if(IAS.registers.IBR!=[0]*20):
            if(verify(operation)):
                operation(IAS,tempo)      
                return   
            operation(IAS)    
            Fetch(address,IAS)
            Execute(address,IAS,tempo)
        else:    
            if(verify(operation)):
                operation(IAS,tempo)
                return         
            operation(IAS)           
    else:
        Fetch(address,IAS) 
        if(IAS.instructions.opcodesCheck(IAS.registers.IR)):
            Execute(address,IAS,tempo)
        else: 
            return  
    
            
    

def solve(address,content,IAS,tempo):
    try:
        Fetch(address,IAS)
        flag = Execute(address,IAS,tempo)
    except Exception as e:
        print("Some error occurred")        
           
            
    
if __name__=="__main__":
    try:
    
        IAS=Computer()

        f = open("./SampleInputs/1.txt",'r')
        numMemoryLocations = int(f.readline())
        count=0
        #input format <address> <value> eg:08B FFFFFFFFFF 
        while(count!=numMemoryLocations):
            count+=1
            mem = str(f.readline()[:-1]).split(" ")
            address=Instructions.convert_HexToDec(mem[0])-1
            content=Instructions.convert_HexToBin(mem[1])

            if(address == -1):
                print("This address is reserved for Start.")
                continue

            #allocating memory with binary values
            for i in range(len(content)):
                IAS.memory.mem[address]=[int(char) for char in content]

        _ = f.readline()
        tempo = {} 
        new_content = [1]*40
        while(new_content[0:8]!='0'*8 or new_content[20:28]!='0'*8 ):
            instruction = str(f.readline()[:-1]).split(" ")
            new_address=Instructions.convert_HexToDec(instruction[0])-1
            new_content=Instructions.convert_HexToBin(instruction[1])

            tempo[new_address] = new_content
            if(new_address == -1):
                print("This address is reserved for Start.")
                continue

            #allocating memory with binary values
            try: 
                if(new_content[0:8]!='0'*8 or new_content[20:28]!='0'*8):
                    for i in range(len(new_content)):
                        IAS.memory.mem[new_address]=[int(char) for char in new_content]
            except Exception as e:
                print('Memory Address not found')

        instructions_list = list(tempo.values())
        address_list = list(tempo.keys())
        for i in range(len(tempo)):
            try:
                if(IAS.registers.PC<len(tempo) and instructions_list[IAS.registers.PC]!=[0]*40):
                    solve(address_list[IAS.registers.PC],instructions_list[IAS.registers.PC],IAS,tempo)
                else:
                    break    
            except Exception as e:
                print("")
    except Exception as e:
        print("Some error occurred.Try \n 1)Verifying the path of the file\n 2)Verifying the input format")
