class test_s:
  def __init__(self,sname='all'):
    self.sname = sname 
    
  def print_name(self, sname):
    print(sname)
    
  def print_name2(self,sname):
    self.print_name(sname)
    
