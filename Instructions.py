#Following methods are for conversions (binary,decimal,hexadecimal)
def convert_HexToDec(string):
    return int(string,16)

def convert_HexToBin(string):    
    bStr = '' 
    for i in range(len(str(string))):
        temp=string[i]
        temp=bin(int(temp,16))[2:].zfill(4)
        bStr+=temp 
    
    return bStr

def convert_BinToDec(string):
    return int(string,2)

def convert_ListToDec(lis):
    s = [str(i) for i in lis]
    string = "".join(s)
    address = convert_BinToDec(string)
    return address
    
def convert_DecToBin(n):  
    temp = bin(n).replace("0b", "")
    return [char for char in temp]
      

#all the instructions are stored in this
class INSTRUCTIONS():
    def __init__(self):
        self.codes={ 
        '00000001': self.LOAD_MX, 
        '00000010': self.LOAD_NEGATIVE_MX,  
        '00000011': self.LOAD_MODULUS_MX, 
        '00000100': self.LOAD_MODULUSNEGATIVE_MX, 
        '00000101': self.ADD_MX, 
        '00000111': self.ADD_MODULUS_MX, 
        '00000110': self.SUB_MX, 
        '00001000': self.SUB_MODULUS_MX, 
        '00001001': self.LOAD_MQ_MX,
        '00001010': self.LOADMQ,
        '00001011': self.MUL_MX, 
        '00001100': self.DIV_MX, 
        '00001101': self.JUMP_MX_LHS,
        '00001110': self.JUMP_MX_RHS,
        '00001111': self.JUMP_CONDITIONAL_MX_LHS,
        '00010000': self.JUMP_CONDITIONAL_MX_RHS,
        '00010100': self.LSH, 
        '00010101': self.RSH, 
        '00100001': self.STOR_MX,
        '00010010': self.STOR_MX_LHS, 
        '00010011': self.STOR_MX_RHS, 
    }

    def LOADMQ(self,IAS):
        IAS.registers.AC = IAS.registers.MQ
        LoadMQtxt = "After Load MQ :\n Accumulator:{AC} \n MQ:{MQ}\n".format(AC = IAS.registers.AC , MQ = IAS.registers.MQ) 
        print(LoadMQtxt)

    def LOAD_MQ_MX(self,IAS):
        try:
            IAS.registers.MBR = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]
            IAS.registers.MQ =IAS.registers.MBR    
            LoadMQMXtxt = "After Load MQ MX:\n MBR:{MBR} \n MQ:{MQ}\n".format(MBR = IAS.registers.MBR , MQ = IAS.registers.MQ)
            print(LoadMQMXtxt)
        except Exception as e:
            print("You are trying to access the memory which does not exist")    
        
    def STOR_MX(self,IAS): 
        IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]=IAS.registers.AC
        STORMXtxt = "After STOR MX :\n M(X):{MX}\n MAR:{MAR}\n".format(MX = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1],MAR=IAS.registers.MAR)
        print(STORMXtxt)

    def LOAD_MX(self,IAS):
        try:
            IAS.registers.MBR = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]
            IAS.registers.AC =IAS.registers.MBR   
            LoadMXtxt = "After Load MX :\n Accumulator:{AC} \n MBR:{MBR}\n".format(AC = IAS.registers.AC , MBR = IAS.registers.MBR)
            print(LoadMXtxt)
        except Exception as e:
            print("You are trying to access the memory which does not exist")

    def LOAD_NEGATIVE_MX(self,IAS):
        try:
            IAS.registers.MBR = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]
            IAS.registers.AC =IAS.registers.MBR
            IAS.registers.AC[0]=1-IAS.registers.AC[0]
            LoadNegativeMXtxt = "After Load -MX :\n Accumulator:{AC} \n MBR:{MBR}\n".format(AC = IAS.registers.AC , MBR = IAS.registers.MBR)
            print(LoadNegativeMXtxt)
        except Exception as e:
            print("You are trying to access the memory which does not exist")    

    def LOAD_MODULUS_MX(self,IAS):
        try:
            IAS.registers.MBR = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]
            IAS.registers.AC =IAS.registers.MBR
            IAS.registers.AC[0]=0
            LoadModulusMXtxt = "After Load |MX| :\n Accumulator:{AC} \n MBR:{MBR}\n".format(AC = IAS.registers.AC , MBR = IAS.registers.MBR)
            print(LoadModulusMXtxt)
        except Exception as e:
            print("You are trying to access the memory which does not exist")    

    def LOAD_MODULUSNEGATIVE_MX(self,IAS):
        try:
            IAS.registers.MBR = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]
            IAS.registers.AC =IAS.registers.MBR
            IAS.registers.AC[0]=1
            LoadNegativeModulusMXtxt = "After Load -|MX| :\n Accumulator:{AC} \n MBR:{MBR}\n".format(AC = IAS.registers.AC , MBR = IAS.registers.MBR)
            print(LoadNegativeModulusMXtxt)
        except Exception as e:
            print("You are trying to access the memory which does not exist")    
            

    def JUMP_MX_LHS(self,IAS,tempo):
        try:
            count =0 
            for i in tempo.keys():
                if(i == convert_ListToDec(IAS.registers.MAR)-1): 
                    IAS.registers.PC = count
                    JUMPMXLHStxt = "After JUMP MX LHS :\n PC:{PC} \n MBR:{MBR}\n".format(PC = IAS.registers.PC , MBR = IAS.registers.MBR)
                    print(JUMPMXLHStxt)
                    return
                count+=1
            
        except Exception as e:
            print("Some error occurred")        

    def JUMP_MX_RHS(self,IAS,tempo):
        try:
            count =0 
            for i in tempo.keys():
                if(i == convert_ListToDec(IAS.registers.MAR)-1): 
                    IAS.registers.PC = count
                    IAS.registers.IBR = [int(char) for char in tempo[i][20:]]
                    IAS.registers.IR = IAS.registers.IBR[:8]
                    IAS.registers.MAR = IAS.registers.IBR[8:]
                    JUMPMXRHStxt = "After JUMP MX RHS :\n PC:{PC} \n MBR:{MBR}\n".format(PC = IAS.registers.PC , MBR = IAS.registers.MBR)
                    print(JUMPMXRHStxt)
                    return
                count+=1
        except Exception as e:
            print("Some error occurred")

    def JUMP_CONDITIONAL_MX_LHS(self,IAS,tempo):
        try:
            if(convert_ListToDec(IAS.registers.AC[1:])>0 and IAS.registers.AC[0]!=1):
                count =0 
                for i in tempo.keys():
                    if(i == convert_ListToDec(IAS.registers.MAR)-1): 
                        IAS.registers.PC = count
                        JUMPConditionalMXLHStxt = "After JUMP CONDITIONAL MX LHS :\n PC:{PC} \n MBR:{MBR}\n".format(PC = IAS.registers.PC , MBR = IAS.registers.MBR)
                        print(JUMPConditionalMXLHStxt)
                        return
                    count+=1     
            else:
                print("Jump condition is not satisfied")
        except Exception as e:
            print("Some error occurred") 

    def JUMP_CONDITIONAL_MX_RHS(self,IAS,tempo):
        try:
            if(convert_ListToDec(IAS.registers.AC[1:])>0 and IAS.registers.AC[0]!=1):
                print(IAS.registers.AC)
                count =0 
                for i in tempo.keys():
                    if(i == convert_ListToDec(IAS.registers.MAR)-1): 
                        IAS.registers.PC = count
                        IAS.registers.IBR = [int(char) for char in tempo[i][20:]]
                        IAS.registers.IR = IAS.registers.IBR[:8]
                        IAS.registers.MAR = IAS.registers.IBR[8:]
                        JUMPConditionalMXRHStxt = "After JUMP CONDITIONAL MX RHS :\n PC:{PC} \n MBR:{MBR}\n".format(PC = IAS.registers.PC , MBR = IAS.registers.MBR)
                        print(JUMPConditionalMXRHStxt)
                        return
                    count+=1     
            else:
                print("Jump condition is not satisfied")
        except Exception as e:
            print("Some error occurred")

    def ADD_MX(self,IAS): 
        try:
            IAS.registers.MBR = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]
            valueA = convert_ListToDec(IAS.registers.MBR[1:])
            valueB =  convert_ListToDec(IAS.registers.AC[1:])

            if(IAS.registers.MBR[0]==1):
                valueA = -1*valueA
            if(IAS.registers.AC[0]==1):
                valueB = -1*valueB

            flag=0
            temp = bin(valueA+valueB).replace("0b","")
            if(temp[0]=='-'):
                flag=1
                temp = temp[1:].rjust(40,"0")
            else:
                temp = temp.rjust(40,"0")    
            IAS.registers.AC = [int(char) for char in temp]
            if(flag):
                IAS.registers.AC[0]=1    
            AddMXtxt = "After ADD MX :\n Accumulator:{AC} \n MBR:{MBR}\n".format(AC = IAS.registers.AC , MBR = IAS.registers.MBR)
            print(AddMXtxt)
        except Exception as e:
            print("Some error occured...Maybe try with addition of smaller values and verify if the address is valid or not")    

    def ADD_MODULUS_MX(self,IAS): 
        try:
            IAS.registers.MBR = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]

            if(IAS.registers.MBR[0]==1):
                IAS.registers.MBR[0] = 0

            valueA = convert_ListToDec(IAS.registers.MBR[1:])
            valueB =  convert_ListToDec(IAS.registers.AC[1:])


            if(IAS.registers.AC[0]==1):
                valueB = -1*valueB

            flag=0 
            temp = bin(valueA+valueB).replace("0b","")
            if(temp[0]=='-'):
                flag = 1
                temp = temp[1:].rjust(40,"0")
            else:
                temp = temp.rjust(40,"0")
            
            IAS.registers.AC = [int(char) for char in temp]
            if(flag):
                IAS.registers.AC[0]=1
        
            AddModulusMXtxt = "After ADD |MX| :\n Accumulator:{AC} \n MBR:{MBR}\n".format(AC = IAS.registers.AC , MBR = IAS.registers.MBR)
            print(AddModulusMXtxt)

        except Exception as e:
            print("Some error occured...Maybe try with addition of smaller values and verify if the address is valid or not")    
        
    def SUB_MX(self,IAS):
        try:
            IAS.registers.MBR = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]
            valueA = convert_ListToDec(IAS.registers.MBR[1:])
            valueB =  convert_ListToDec(IAS.registers.AC[1:])

            if(IAS.registers.MBR[0]==1):
                valueA = -1*valueA
            if(IAS.registers.AC[0]==1):
                valueB = -1*valueB

            flag=0 
            temp = bin(valueB-valueA).replace("0b","")
            if(temp[0]=='-'):
                flag=1
                temp = temp[1:].rjust(40,"0")
            else:
                temp = temp.rjust(40,"0")    
            IAS.registers.AC = [int(char) for char in temp]
            if(flag):
                IAS.registers.AC[0]=1
            SubMXtxt = "After SUB MX :\n Accumulator:{AC} \n MBR:{MBR}\n".format(AC = IAS.registers.AC , MBR = IAS.registers.MBR)
            print(SubMXtxt) 

        except Exception as e:
            print("Some error occured...Maybe try with subtraction of smaller values and verify if the address is valid or not")   
                
    def SUB_MODULUS_MX(self,IAS):
        try:
            IAS.registers.MBR = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]

            if(IAS.registers.MBR[0]==1):
                IAS.registers.MBR[0] = 0

            valueA = convert_ListToDec(IAS.registers.MBR[1:])
            valueB =  convert_ListToDec(IAS.registers.AC[1:])


            if(IAS.registers.AC[0]==1):
                valueB = -1*valueB

            flag=0 
            temp = bin(valueB-valueA).replace("0b","")
            if(temp[0]=='-'):
                flag = 1
                temp = temp[1:].rjust(40,"0")
            else:
                temp = temp.rjust(40,"0")
            
            IAS.registers.AC = [int(char) for char in temp]
            if(flag):
                IAS.registers.AC[0]=1 
            SubModulusMXtxt = "After SUB |MX| :\n Accumulator:{AC} \n MBR:{MBR}\n".format(AC = IAS.registers.AC , MBR = IAS.registers.MBR)
            print(SubModulusMXtxt)
        except Exception as e:
            print("Some error occured...Maybe try with subtraction of smaller values and verify if the address is valid or not")        

    def MUL_MX(self,IAS):
        try:
            IAS.registers.MBR = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]
            valueA = convert_ListToDec(IAS.registers.MBR[1:])
            valueB =  convert_ListToDec(IAS.registers.AC[1:])

            if(IAS.registers.MBR[0]==1):
                valueA = -1*valueA
            if(IAS.registers.AC[0]==1):
                valueB = -1*valueB

            flag=0 
            temp = bin(valueA*valueB).replace("0b","")

            if(temp[0]=='-'):
                flag=1
                temp = temp[1:].rjust(80,"0")
            else:
                temp = temp.rjust(80,"0")    

            IAS.registers.AC = [int(char) for char in temp][:40]
            IAS.registers.MQ = [int(char) for char in temp][40:]

            if(flag):
                IAS.registers.AC[0]=1    
            MULMXtxt = "After MUL MX :\n Accumulator:{AC} \n MBR:{MBR}\n MQ:{MQ}\n".format(AC = IAS.registers.AC , MBR = IAS.registers.MBR,MQ=IAS.registers.MQ)
            print(MULMXtxt)
        except Exception as e:
            print("Some error occured...Maybe try with multiplication of smaller values and verify if the address is valid or not")   

    def DIV_MX(self,IAS):
        try:
            IAS.registers.MBR = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1]
            valueA = convert_ListToDec(IAS.registers.MBR[1:])
            valueB =  convert_ListToDec(IAS.registers.AC[1:])

            if(valueA==0):
                print("Division with 0 is not feasible")
                return 

            if(IAS.registers.MBR[0]==1):
                valueA = -1*valueA
            if(IAS.registers.AC[0]==1):
                valueB = -1*valueB

            flag=0 
            temp = bin(int(valueB/valueA)).replace("0b","")
            temp2 = bin(int(valueB%valueA)).replace("0b","")
            temp2.rjust(40,"0")
		
            if(temp[0]=='-'):
                flag=1
                temp = temp[1:].rjust(40,"0")
            else:
                temp = temp.rjust(40,"0")    

            IAS.registers.AC = [int(char) for char in temp]
            IAS.registers.MQ = [int(char) for char in temp2]

            if(flag):
                IAS.registers.AC[0]=1    
            DIVMXtxt = "After DIV MX :\n Accumulator:{AC} \n MBR:{MBR}\n MQ:{MQ}\n".format(AC = IAS.registers.AC , MBR = IAS.registers.MBR,MQ=IAS.registers.MQ)
            print(DIVMXtxt)
        except Exception as e:
            print("Some error occured...Maybe try with divison of different values and verify if the address is valid or not") 

    def LSH(self,IAS):
        try:
            temp = convert_ListToDec(IAS.registers.AC)
            temp<<=1
            IAS.registers.AC = bin(IAS.registers.AC).replace("0b","").rjust(40,"0")
            LSHtxt = "After LSH :\n Accumulator:{AC}\n".format(AC = IAS.registers.AC)
            print(LSHtxt)
        except Exception as e:
            print('Some error occured...')    

    def RSH(self,IAS):
        try:
            temp = convert_ListToDec(IAS.registers.AC)
            temp>>=1
            IAS.registers.AC = bin(IAS.registers.AC).replace("0b","").rjust(40,"0")
            RSHtxt = "After RSH :\n Accumulator:{AC}\n".format(AC = IAS.registers.AC)
            print(RSHtxt)
        except Exception as e:
            print('Some error occured...')    

    def STOR_MX_LHS(self,IAS):
        try:
            IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1][8:20] = IAS.registers.AC[28:40] 
            STORMXLHStxt = "After STOR MX LHS :\n M(X):{MX}\n MAR:{MAR}\n".format(MX = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1],MAR=IAS.registers.MAR)
            print(STORMXLHStxt)
        except Exception as e:
            print('Memory location does not exist')     
          
    def STOR_MX_RHS(self,IAS):
        try:
            IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1][28:40] = IAS.registers.AC[28:40]
            STORMXRHStxt = "After STOR MX RHS:\n M(X):{MX}\n MAR:{MAR}\n".format(MX = IAS.memory.mem[convert_ListToDec(IAS.registers.MAR)-1],MAR=IAS.registers.MAR)
            print(STORMXRHStxt)
        
        except Exception as e:
            print('Some error occured...')    

    #checks whether the instruction code is valid or not
    def opcodesCheck(self,checkList):
       s = [str(i) for i in checkList] 
       string = ("".join(s)) 
       if string in self.codes:
           return self.codes[string]
       return False
