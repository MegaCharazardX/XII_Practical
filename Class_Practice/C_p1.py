import os
class File_Reader :
    global FileNotFoundError, FileExistsError, FileIsNotFoundMsg
    FileNotFoundError = "FileNotFoundError"
    FileExistsError = "FileExistsError"
    
    FileIsNotFoundMsg = "File Is Not Found"
    
    def __init__(self,
                 _file_name : str
                 ):
            self.file_name = _file_name
            
    def Read_File (self):
        err_name = ""
        file_path = f"Text_Files/{self.file_name}.txt"
        try :
            if os.path.exists(file_path) :
                self._file = open(file_path, "r")
            self.__ans = ""
            line = self._file.readline()
            for i in line.split():
                self.__ans = self.__ans +  f"{i} "
                #print()    
            
        except Exception as err:
            err_name = f"{type(err)}"
        
        finally :
            if err_name == FileNotFoundError or err_name == FileExistsError :
                pass
            else :
                print(self.__ans)
                print("File Closed")

            
file_reader = File_Reader("p1")
file_reader.Read_File()