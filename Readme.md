# IAS Computer Architecture

## Running Instructions:
  * _Open terminal in current folder_
  * _Run '<python3 IAS.py>'_
  * _Sample Input has been given in **SampleInput** folder._
    * In order to test with different inputs,update the path **f = open("./SampleInputs/1.txt",'r')**(_line 82 of IAS.py file_).
    ```
    eg: f = open("./SampleInputs/2.txt","r") 
    ```

## Requirements 
  * _python3(Recommended version:Python 3.7.6)_

## Important Notes
  * _Input must be in Hexadecimal format without mention of 0x at begining._   
      ```
      eg: ~~0x08A 0x0111105112~~ is incorrect.
          08A 0111105112 is correct.
      ```

  * _Hexadecimal Instruction/Data must be of 10 digits and Hexadecimal address must be of 3 digits.If any digits were missing automatically 0s or garbage will be replaced in their place._

  * _There must be space(" ") in between address and Instruction/Data._
  * _The sample output screenshots are placed in **Screenshots** folder._ 